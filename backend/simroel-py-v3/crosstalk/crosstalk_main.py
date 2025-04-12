import numpy as np
from numpy import (
    power,
    stack,
    any,
    unique,
    arange,
    max
)
from itertools import product
from pandas import DataFrame, MultiIndex, Series
from auxiliar.constants import PROPAGATION_CONSTANT, MCF_CONFIGS
from auxiliar.functions import linear_to_db
from auxiliar.functions import plot_xt_table

class CrosstalkMain(object):
    def __init__(self,
                 xt_utils,
                 router,
                 connection_dict,
                 coupling_coeff,
                 bending_radius,
                 core_pitch,
                 n_cores,
                 edges):
        self.xt_utils = xt_utils
        self.router = router
        self.connection_dict = connection_dict
        self.coupling_coeff = coupling_coeff
        self.bending_radius = bending_radius
        self.core_pitch = core_pitch
        self.mcf_adj_cores = MCF_CONFIGS[n_cores]["adjs"]
        self.h = 2 * ((power(self.coupling_coeff, 2) / PROPAGATION_CONSTANT) * (self.bending_radius / self.core_pitch))
        self.xt_matrix = DataFrame(columns=arange(n_cores), index=MultiIndex.from_tuples(edges)).fillna(0.)

    @staticmethod
    def has_crosstalk(fiber, connection, route, adjacent_cores):

        condition = stack([
            fiber[link][adjacent_cores, connection.fiber_slot:connection.fiber_slot + int(connection.slots)]
            for link in route
        ])
        return any(condition >= 0)

    def calculate(self, connection, fiber, route, increment=True):
        """
        P_XT = sum(I_ij * P_j * h * L) for all adjacent cores, where:
        h = 2 * ( k^2 / β ) * ( R / Λ ),
        I_ij = N_ij / N_j
        """

        link_legth = self.router.calc_weight(route) * 1e3
        result_per_link = self.overlapping_index(fiber, connection)

        p_xt_list = list()
        px_xt_buffer = self.xt_matrix.copy()
        for link, L in zip(route, link_legth):
            i_ji_per_core, xt_required = result_per_link[link]
            if i_ji_per_core:
                for core, i_ji_power in i_ji_per_core.items():
                    p_xt_linear_buff = (i_ji_power * self.h * L) / connection.power
                    p_xt_linear = p_xt_linear_buff + self.xt_matrix.loc[link, core]
                    p_xt_db = linear_to_db(p_xt_linear)
                    p_xt_list.append((core, link, p_xt_linear_buff))
                    if p_xt_db >= xt_required[core]:
                        return False

        for record in p_xt_list:
            (core, link, p_xt) = record
            if increment:
                connection.p_xt = p_xt
                self.xt_matrix.loc[link, core] += p_xt  # linear
            else:
                xt_core = self.xt_matrix.loc[link, core]
                if xt_core - connection.p_xt >= 0:
                    self.xt_matrix.loc[link, core] -= connection.p_xt
                else:
                    self.xt_matrix.loc[link, core] = 0
        return True

    def overlapping_index(self, fiber, connection):
        adjacent_cores = self.mcf_adj_cores[connection.fiber_core]

        result_per_link = dict()
        for link in connection.route:
            arr = fiber.fiber_data[link][adjacent_cores, connection.fiber_slot:connection.fiber_slot + int(connection.slots)]
            conn_idx, n_ij = unique(arr[arr >= 0], return_counts=True)

            if n_ij.sum() == 0:
                result_per_link[link] = [{}, {}]
                continue

            n_j = [self.connection_dict[index].slots for index in conn_idx]
            n_power = [self.connection_dict[index].power for index in conn_idx]
            conns_per_core = dict(zip(adjacent_cores, [unique(row[row >= 0]).tolist() for row in arr]))
            conns_per_core[connection.fiber_core] = [connection.iid]
            conns_per_core = {core: n for core, n in conns_per_core.items() if n}

            xt_required = {
                k: max([self.xt_utils.get_cross_required(self.connection_dict[idx].size,
                                                         self.connection_dict[idx].modulation)
                        for idx in v ])
                for k, v in conns_per_core.items()
            }

            i_ij = (n_ij / n_j) * n_power
            i_ji = (n_ij / (connection.slots - 1)) * connection.power

            i_ij_per_conn = dict(zip(conn_idx, i_ij))
            i_ji_per_conn = dict(zip(conn_idx, i_ji))
            i_ji_per_conn[connection.iid] = sum([i_ij_per_conn[iid] for iid in conn_idx])

            # i_ji_per_core = {
            #     adjacent_cores[index]: sum([i_ji_per_conn.get(conn_id, 0) for conn_id in unique(arr[index, :])])
            #     for index in range(arr.shape[0])
            # }
            # i_ji_per_core[connection.fiber_core] = sum([i_ij_per_conn.get(conn_id, 0) for conn_id in n_ij])

            i_ji_per_core = {
                core: sum([i_ji_per_conn[iid] for iid in n]) for core, n in conns_per_core.items()
            }

            # i_ji_per_core = {k: v for k, v in i_ji_per_core.items() if v in xt_required.keys()}
            result_per_link[link] = [i_ji_per_core, xt_required]

        return result_per_link

    # def overlapping_index(self, fiber, connection):
    #     adjacent_cores = self.mcf_adj_cores[connection.fiber_core]
    #
    #     result_per_link = dict()
    #     for link in connection.route:
    #         arr = fiber.fiber_data[link][adjacent_cores, connection.fiber_slot:connection.fiber_slot + int(connection.slots)]
    #         print(arr)
    #         conn_idx, n_ij = unique(arr[arr >= 0], return_counts=True)
    #         n_j = [self.connection_dict[index].slots for index in conn_idx]
    #         n_power = [self.connection_dict[index].power for index in conn_idx]
    #
    #         conns_per_core = dict(zip(adjacent_cores, [unique(row[row >= 0]).tolist() for row in arr]))
    #         conns_per_core[connection.fiber_core] = [connection.iid]
    #
    #         xt_required = {
    #             k: max([self.xt_utils.get_cross_required(self.connection_dict[idx].size,
    #                                                      self.connection_dict[idx].modulation)
    #                     for idx in v])
    #             for k, v in conns_per_core.items() if v
    #         }
    #
    #         print('conns_per_core',conns_per_core)
    #         print('xt_required', xt_required)
    #         if n_ij.sum() == 0:
    #             result_per_link[link] = [{}, {}]
    #             continue
    #
    #         i_ij = (n_ij / n_j) * n_power
    #         i_ji = (n_ij / (connection.slots - 1)) * connection.power
    #
    #         i_ij_per_conn = dict(zip(conn_idx, i_ij))
    #         i_ji_per_conn = dict(zip(conn_idx, i_ji))
    #
    #         i_ji_per_core = {
    #             adjacent_cores[index]: sum([i_ji_per_conn.get(conn_id, 0) for conn_id in unique(arr[index, :])])
    #             for index in range(arr.shape[0])
    #         }
    #         i_ji_per_core[connection.fiber_core] = sum([i_ij_per_conn.get(conn_id, 0) for conn_id in n_ij])
    #         i_ji_per_core = {k: v for k, v in i_ji_per_core.items() if v in xt_required.keys()}
    #         print('i_ji_conn',i_ji_per_conn)
    #         print('i_ij_per_conn',i_ij_per_conn)
    #         print('i_ji_per_core', i_ji_per_core)
    #         print(connection.iid)
    #         result_per_link[link] = [i_ji_per_core, xt_required]
    #
    #     return result_per_link