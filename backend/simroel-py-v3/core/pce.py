from numpy import (
    ndarray,
    array,
    zeros_like
)
from crosstalk.crosstalk_main import CrosstalkMain
from routing.router import Router
from utils.modulation import Modulation
from utils.assignment import Assignment
from utils.fiber import Fiber
from utils.connection import Connection
from osnr.osnr_main import OSNR
from typing import Callable, List, Dict


class PCE(object):
    def __init__(self,
                 fiber: Fiber,
                 crosstalk: CrosstalkMain,
                 router: Router,
                 modulation: Modulation,
                 modulations: List[str],
                 assignment: Assignment,
                 k_paths: int,
                 core_selection_fn: Callable,
                 cores: List[int],
                 osnr: OSNR,
                 mcf_config: Dict[int, dict],
                 dict_connections: Dict[int, Connection]
                 ):
        self.fiber = fiber
        self.crosstalk = crosstalk
        self.router = router
        self.modulation = modulation
        self.modulations = modulations
        self.assigment = assignment
        self.k_paths = k_paths
        self.core_selection_fn = core_selection_fn
        self.cores = cores
        self.osnr = osnr
        self.mcf_config = mcf_config
        self.dict_connections = dict_connections

        self.power_strategy = array([6, 5, 4, 3, 2, 0.8, 0.5]) * 1e-4  # botar reverso

    def process(self, pcep, fes, stats):
        # NLI -> power, fiber_core, slots, fiber_slot, rota
        # OSNR -> power, rota

        for connection in pcep.conn_list:
            routes = self.router.shortest_paths(connection.src, connection.tgt, k=self.k_paths)
            conn_osnr = 0
            for k, route in enumerate(routes):
                skip_cores = set()
                connection.update(modulation=self.modulations[0], route=route)

                osnr_mask = []# zeros_like(self.power_strategy, dtype=bool)
                for i, power in enumerate(self.power_strategy):
                    connection.update(power=power)
                    osnr_validation = self.osnr.validate(route, connection, self.fiber, k)
                    if not osnr_validation:
                        break
                    osnr_mask.append(power)

                # if self.osnr.validate(route, connection, self.fiber, k):
                if any(osnr_mask):

                    for modulation in self.modulations:
                        cores = self.core_selection_fn(self.cores)

                        for core_idx, core in enumerate(cores):
                            if core not in skip_cores:
                                connection.update(
                                    modulation=modulation,
                                    slots=self.modulation.calculate_n_slots(modulation, connection)
                                )

                            if self.assigment.alloc(connection, self.fiber, route, core):

                                # ---------------------------------estratégia 1  -> Maior OSNR (ASE+NLI) -----------------------------------------------------
                                # conn_pw = 0.0003
                                # for pw in osnr_mask:
                                #     connection.update(power=pw)
                                #     pw_osnr = self.osnr.validate(route, connection, self.fiber.fiber_data, k, validation="estrategia_1")
                                #     if conn_osnr < pw_osnr:
                                #         conn_osnr = pw_osnr
                                #         conn_pw = pw
                                # connection.update(power=conn_pw)
                                # ---------------------------------estratégia 2  -> menor potencia -> Menor XT ------------------------------------------------
                                for pw in osnr_mask:
                                    connection.update(power=pw)
                                    pw_osnr = self.osnr.validate(route, connection, self.fiber.fiber_data, k,
                                                                 validation="estrategia_2")
                                    if not pw_osnr:
                                        osnr_mask.remove(pw)
                                if len(osnr_mask) > 0:
                                    connection.update(power=min(osnr_mask))
                                ####################################################################################################################
                                if self.osnr.validate(route, connection, self.fiber.fiber_data, k, validation="nli"):
                                    adjacent_cores = self.mcf_config["adjs"][core]

                                    if self.crosstalk.has_crosstalk(self.fiber.fiber_data, connection, route,
                                                                    adjacent_cores):
                                        if self.crosstalk.calculate(connection, self.fiber, route):
                                            alloc_status = "allocated"
                                            break
                                        else:
                                            alloc_status = "crosstalk"
                                            self.fiber.free(connection)
                                            break  # next core
                                    else:
                                        alloc_status = "allocated"
                                        break

                                else:
                                    alloc_status = "nli"
                                    self.fiber.free(connection)
                                    continue  # next core

                            else:
                                alloc_status = "resource"
                                skip_cores.add(core)
                                continue  # next core

                        if alloc_status == "allocated" or alloc_status == "nli":
                            break

                    if alloc_status == "allocated" or len(skip_cores) == len(self.cores):
                        break

                else:
                    alloc_status = "osnr"
                    break

            self.dict_connections[connection.iid] = connection
            if stats.block_control(alloc_status):
                pcep.add_conn_assigned(connection)
                connection.update(release=connection.sim_clock + connection.hold)
                fes.insert(connection, connection.release)

                if connection.sim_clock == -1:
                    raise ValueError("connection.simclock == -1")

            else:
                connection.update(fiber_slot=-1)

        pcep.conn_list.clear()

    def process_2(self, pcep, fes, stats):  # normal
        for connection in pcep.conn_list:
            routes = self.router.shortest_paths(connection.src, connection.tgt, k=self.k_paths)

            for k, route in enumerate(routes):
                skip_cores = set()
                connection.update(modulation=self.modulations[0])
                is_alloc = self.osnr.validate(route, connection, self.fiber, k)

                if is_alloc:
                    for modulation in self.modulations:
                        cores = self.core_selection_fn(self.cores)

                        for core_idx, core in enumerate(cores):
                            if core not in skip_cores:
                                connection.update(
                                    modulation=modulation,
                                    slots=self.modulation.calculate_n_slots(modulation, connection)
                                )
                            is_alloc = self.assigment.alloc(connection, self.fiber, route, core)
                            if is_alloc:
                                is_alloc = self.osnr.validate(route, connection, self.fiber.fiber_data, k,
                                                              validation="nli")
                                if is_alloc:
                                    adjacent_cores = self.mcf_config["adjs"][core]

                                    if self.crosstalk.has_crosstalk(self.fiber.fiber_data, connection, route,
                                                                    adjacent_cores):
                                        if self.crosstalk.calculate(connection, self.fiber, route):
                                            alloc_status = "allocated"
                                            break
                                        else:
                                            alloc_status = "crosstalk"
                                            self.fiber.free(connection)
                                            break  # next core
                                    else:
                                        alloc_status = "allocated"
                                        break

                                else:
                                    alloc_status = "nli"
                                    self.fiber.free(connection)
                                    continue  # next core

                            else:
                                alloc_status = "resource"
                                skip_cores.add(core)
                                continue  # next core

                        if alloc_status == "allocated" or alloc_status == "nli":
                            break

                    if alloc_status == "allocated" or len(skip_cores) == len(self.cores):
                        break

                else:
                    alloc_status = "osnr"
                    break

            self.dict_connections[connection.iid] = connection
            if stats.block_control(alloc_status):
                pcep.add_conn_assigned(connection)
                connection.update(release=connection.sim_clock + connection.hold)
                fes.insert(connection, connection.release)

                if connection.sim_clock == -1:
                    raise ValueError("connection.simclock == -1")

            else:
                connection.update(fiber_slot=-1)

        pcep.conn_list.clear()

    def release_connnection(self, connection):
        adjacent_cores = self.mcf_config["adjs"][connection.fiber_core]
        if self.crosstalk.has_crosstalk(self.fiber.fiber_data, connection, connection.route, adjacent_cores):
            self.crosstalk.calculate(connection, self.fiber, connection.route, increment=False)
        self.fiber.free(connection)
        # del self.dict_connections[connection.iid]
