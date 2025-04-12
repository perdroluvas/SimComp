import numpy as np
import pandas as pd
from tqdm import tqdm
from fes import FESControl
from pcc import PathComputationClient
from pcep import PathComputationElement
from core.pce import PCE
from files.parameters import Params
from routing.router import Router
from utils.assignment import Assignment
from utils.fiber import Fiber
from utils.modulation import Modulation
from utils.connection import Connection
from utils.stats import Statistics
from crosstalk.crosstalk_main import CrosstalkMain
from crosstalk.crosstalk_utils import CrosstalkUtils
from osnr.osnr_main import OSNR
from osnr.osnr_utils import OSNRUtils
from auxiliar.functions import plot_xt_table
import time


class Simulation(object):
    def __init__(self):
        self.params = Params()
        self.OSNR_Utils = OSNRUtils(self.params.get_osnr_table())
        self.router = Router(self.params.get_topology_info()['graph'])
        self.fiber = Fiber(self.params.get_n_cores(),
                           self.params.get_slot_size(),
                           self.params.get_bandwidth(),
                           self.params.get_topology_info()['edges'])
        self.OSNR = OSNR(self.params.get_lambda(),
                         self.params.get_fn(),
                         self.params.get_band_ref(),
                         self.params.get_span_length(),
                         self.params.get_node_loss(),
                         self.params.get_limit_single_carrier(),
                         self.router,
                         self.OSNR_Utils)

        self.assignment = Assignment(self.params.get_allocation_type())

        self.modulation = Modulation(self.params.get_guard_band(),
                                     self.params.get_slot_size(),
                                     self.params.get_modulation(),
                                     self.params.get_limit_single_carrier())
        self.stats = Statistics()
        self.crosstalk_utils = CrosstalkUtils(self.params.get_xt_table())
        self.dict_connections = dict()
        self.crosstalk = CrosstalkMain(self.crosstalk_utils,
                                       self.router,
                                       self.dict_connections,
                                       self.params.get_coupling_coeff(),
                                       self.params.get_bending_radius(),
                                       self.params.get_core_pitch(),
                                       self.params.get_n_cores(),
                                       self.params.get_topology_info()['edges'])
        self.pce = PCE(self.fiber,
                       self.crosstalk,
                       self.router,
                       self.modulation,
                       self.params.get_modulation(),
                       self.assignment,
                       self.params.get_k_routes(),
                       self.params.get_allocation_fn(),
                       self.params.get_cores(),
                       self.OSNR,
                       self.params.get_mcf_config(),
                       self.dict_connections)
        self.fes = FESControl()
        self.pcc = PathComputationClient(None, self.params)

        self.traffic_lambda = self.params.get_traffic_lambda()
        self.conn_types = self.params.get_traffic_conn_types()
        self.arrive_time = 0.0
        self.conn_hold_time = self.params.get_conn_holding_time()
        self.pcc_hold_time = self.params.get_pcc_holding_time()
        self.n_connections = self.params.get_n_connections()
        self.power = self.params.get_p()
        self.n_simulations = self.params.get_n_simulations()
        self.lim_single_carrier = self.params.get_limit_single_carrier()
        self.links = self.params.get_topology_info()['nodes']

        self.pccs = [PathComputationClient(node, self.params) for node in self.links]
        self.pcep = PathComputationElement(self.pccs)

        # =================
        self.get_traffic_sample = self.test_read_file()

    @staticmethod
    def test_read_file():
        sheet = r"../data/2022-09-09-15-06-46-traffic.csv"
        df = pd.read_csv(sheet, sep=";", skipfooter=6, engine="python").drop("Unnamed: 8", axis=1)
        df = df.astype({"SimulationNum": int,
                        "Connection": int,
                        "Size": np.float16,
                        "Arrive_Time": np.float64,
                        "Holdtime": np.float64,
                        "Release_Time": np.float64,
                        "Source": int,
                        "Target": int})
        df["Source"] -= 1
        df["Target"] -= 1

        for row in df.itertuples():
            yield row

    def simulate(self, n_simulation, n_sim_total):
        conn_arrived = 0
        with tqdm(total=self.n_connections, desc=f"Simulation #{n_simulation} of {n_sim_total}") as pbar:
            while True:
                if self.fes.is_empty():
                    connection = self.create_connection(conn_arrived)
                    self.dict_connections[conn_arrived] = connection
                    conn_arrived += 1
                    pbar.update(1)
                else:
                    if self.n_connections > conn_arrived:
                        if self.fes.compare_min(connection.arrive):
                            connection = self.create_connection(conn_arrived)
                            self.dict_connections[conn_arrived] = connection
                            conn_arrived += 1
                            pbar.update(1)
                        else:
                            self.fes_control()
                    else:
                        self.fes_control()

                if (self.n_connections < conn_arrived) or (self.fes.is_empty()):
                    print("BREAK!")
                    break

    def create_connection(self, index):
        interval_arrive = np.random.exponential(self.traffic_lambda)
        source = np.random.choice(self.links)
        target = np.random.choice(self.links[self.links != source])
        size = np.random.choice(self.conn_types)
        self.arrive_time += interval_arrive

        connection = Connection(
            iid=index,
            src=source,
            tgt=target,
            size=size,
            hold=np.random.exponential(self.conn_hold_time),
            arrive=self.arrive_time,
            guard_band=self.params.get_guard_band(),
            mcf_fiber_config=self.params.get_mcf_config()
        )
        connection.id_src = source
        connection.id_tgt = target
        connection.power = self.power * np.round(np.ceil(size / self.lim_single_carrier), 4)

        self.stats.handled()

        pcc_index = self.pcc.get_pcc_index(source, self.pccs)
        if self.pccs[pcc_index].get_n_conn() == 0:
            self.fes.insert(self.pccs[pcc_index], connection.arrive + self.pcc_hold_time)

        connection.sim_clock = connection.arrive + self.pcc_hold_time
        self.pccs[pcc_index].add_connection(connection)

        return connection

    def create_connection_v2(self):
        _, _, index, size, arrive, hold, _, source, target = next(self.get_traffic_sample)

        connection = Connection(
            iid=index,
            src=source,
            tgt=target,
            size=size,
            hold=hold,
            arrive=arrive,
            params=self.params
        )
        connection.id_src = source
        connection.id_tgt = target
        connection.power = self.power * np.round(np.ceil(size / self.lim_single_carrier), 4)

        self.stats.handled()

        pcc_index = self.pcc.get_pcc_index(source, self.pccs)
        if self.pccs[pcc_index].get_n_conn() == 0:
            self.fes.insert(self.pccs[pcc_index], arrive + self.pcc_hold_time)

        connection.sim_clock = arrive + self.pcc_hold_time
        self.pccs[pcc_index].add_connection(connection)

        return connection

    def fes_control(self):
        obj_min = self.fes.get_min()[1]
        if isinstance(obj_min, PathComputationClient):
            pcc_index = obj_min.get_pcc_index(obj_min.node, self.pccs)
            self.pcep.add_conn_list(self.pccs[pcc_index].queue_connections)

            if self.fes.remove_min():
                self.pccs[pcc_index].clear_queue()
                self.pce.process(self.pcep, self.fes, self.stats)
                return 0
            else:
                print("[!] ERROR REMOVING PCC")
                return -1
        elif isinstance(obj_min, Connection):
            self.remove_connection(obj_min)
            return 1
        return -1

    def remove_connection(self, conn):
        pcc_index = self.pcc.get_pcc_index(conn.src, self.pccs)
        self.pce.release_connnection(conn)
        if self.fes.remove_min():
            self.pccs[pcc_index].remove_connection(conn)
