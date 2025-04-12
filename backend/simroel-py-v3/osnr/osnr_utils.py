from pandas import DataFrame
from numpy import flip
from itertools import takewhile

class OSNRUtils(object):
    def __init__(self, osnr_required_table: DataFrame):
        self.osnr_required_table = osnr_required_table

    def get_osnr_required(self, conn_size, modulation):
        #conn_size = str(float(conn_size))
        assert (conn_size in self.osnr_required_table.columns), \
            f"[OSNR] Invalid `conn_type` for this BER"
        assert (modulation in self.osnr_required_table.index), \
            f"[OSNR] Invalid `modulation` for this BER"
        return self.osnr_required_table.loc[modulation, conn_size]

    @staticmethod
    def count_adj_connections(slots, connection, route, offset=2):
        adj_conn = dict()
        initial_slot = max(-1, connection.fiber_slot - offset)
        final_slot = min(slots.shape[0] - 1, int(connection.slots) + connection.fiber_slot + 1)

        left = sum(1 for _ in takewhile(lambda x: x >= 0, flip(slots[:initial_slot + 1])))
        right = sum(1 for _ in takewhile(lambda x: x >= 0, slots[final_slot:]))
        if left + right == 0:
            return adj_conn

        adj_conn[route] = adj_conn.get(route, [])
        # (size, initial, final)
        if left > 0:
            adj_conn[route].append((left, initial_slot - left + 1, initial_slot))

        if right > 0:
            adj_conn[route].append((right, final_slot, final_slot + right - 1))

        return adj_conn
