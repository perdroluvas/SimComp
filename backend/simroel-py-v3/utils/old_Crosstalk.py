import math
from .old_crosstalk_utils import CrosstalkUtils
from routing.router import Router
import numpy as np
class Crosstalk:
    def __init__(self, params):
        self.coupling_coeff = 1.2 * (math.pow(10, -2))
        self.propagation_const = math.pow(10, 7)
        self.bending_radius = params.get_bending_radius()
        self.core_pitch = params.get_core_pitch() * math.pow(10, -5)
        self.crosstalkUtils = CrosstalkUtils()
    def hascrosstalk(self, core, slot, conn_size, routes, mcf, fiber):
        Xt_route = dict()
        #print(f'routes: {routes}')
        for route in routes:
            #print(route)
            alocationtabble = fiber.fiber_data[route]
            Xt = dict()
            #print(slot)
            #print(conn_size)
            slot_alloc = list(range(slot, slot + conn_size))
            #print(f'slot_alloc:{slot_alloc}')
            for core_adj in mcf["adjs"][core]:
                slot_adj = []
                xt_rec = []
                for slot_xt in slot_alloc:
                    if alocationtabble[core_adj][slot_xt] == 0:
                        xt_rec.append(slot_xt)
                        slot_adj.append(slot_xt)
                        Xt[core_adj] = slot_adj
                        Xt[core] = xt_rec
                        # Xt.append(core_adj)
                        # Xt.append(core)
                        #add todos os slots adjacentes e o core
                    else:
                        pass
            if Xt != {}:
                Xt_route[route] = Xt
        if Xt_route == {}:
            return False
        else:
            return Xt_route

    # #transformar xt_tabble em um dict
    def CalculateCrosstalk(self, xt_tabble, cores_dict, allocate, conn_size, l, modulation, size):
        control = 0
        #xt_tabble_aux = xt_tabble.copy()
        aux_xt = xt_tabble.copy()

        for route in cores_dict.keys():
            #aux_xt_route = aux_xt[route].copy()  # auxiliar
            xt_route = aux_xt[route].copy()  # xtrota

            xt = 2 * ((math.pow(self.coupling_coeff, 2) / self.propagation_const) * (
                    self.bending_radius / self.core_pitch)) * l
            #print(f'xt: {xt}')
            if allocate:
                for core_xt in cores_dict[route].keys():
                    #print(f'rota {route} antes: {aux_xt}')
                    xt_route[core_xt] += (xt * (len(cores_dict[route][core_xt]) / conn_size))
                    req = self.crosstalkUtils.get_xt_req(size, modulation)
                    xt_route_db = 10 * np.log10(xt_route[core_xt])
                    #print(xt_route_db)
                    if xt_route_db < req:
                        #print(f'conn blocked req:{req}, xt: {xt_route_db}')
                        control += 1
                    else:
                        aux_xt[route] = xt_route.copy()

            if not allocate:
                for core_xt in cores_dict[route].keys():
                    xt_route[core_xt] -= (xt * (len(cores_dict[route][core_xt]) / conn_size))
                    aux_xt[route] = xt_route.copy()
            # if control == 0:
            #     xt_tabble_aux[route] = xt_route.copy()
        if control == 0:
            xt_tabble = aux_xt.copy()
            allocstatus = True
        else:
            allocstatus = False
        return xt_tabble, allocstatus


    def get_xt_tabble(self, ncores, routes):
        xt_aux = np.zeros(ncores)
        xt_tabble = dict()
        for route in routes:
            xt_tabble[route] = xt_aux.copy()
        return xt_tabble
#converter XT para DB