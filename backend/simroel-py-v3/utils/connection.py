from numpy import (
    sum,
    ndarray,
    where,
    any,
    argmax,
    nan,
    zeros,
    uint8,
    isnan,
    flip,
    nonzero
)
from itertools import takewhile
from auxiliar.constants import ALLOCATED


class Connection(object):
    def __init__(self,
                 iid,
                 src,
                 tgt,
                 size,
                 hold,
                 arrive,
                 guard_band,
                 mcf_fiber_config
                 ):
        self.iid = iid
        self.src = src
        self.tgt = tgt
        self.size = size
        self.hold = hold
        self.arrive = arrive
        self.guard_band = guard_band
        self.mcf_guard_band = mcf_fiber_config

        self.in_xt = nan
        self.slots = -1
        self.release = 0.0
        self.fiber_core = -1
        self.fiber_slot = -1
        self.route = []
        self.id_src = -1
        self.id_tgt = -1
        self.modulation = ""
        self.power = 0.0
        self.sim_clock = -1
        self.fiber_cross = None
        self.free_slots = []
        self.p_xt = 0

    def __eq__(self, other):
        return self.iid == other.iid

    def __repr__(self):
        return "<{}({})>".format(
            self.__class__.__name__,
            ", ".join("{}={!r}".format(k, v.shape if isinstance(v, ndarray) else v) for k, v in self.__dict__.items())
        )

    def update(self, **kwargs):
        self.__dict__.update(kwargs)

    def _calculate_in_xt(self, adjacent_cores: ndarray, fiber: ndarray):
        arr = fiber[adjacent_cores, :]
        # take the connection allocation window
        adjacent_slots = arr[:, self.fiber_slot:self.fiber_slot+self.slots]
        bool_mask = adjacent_slots == ALLOCATED
        indices = where(
            any(bool_mask, axis=1),  # if there's any conn slot allocated at adj positions
            argmax(bool_mask, axis=1),  # take the argmax to get the index
            nan  # else, assign NaN
        )
        count_adjs = sum(bool_mask, axis=1)  # count adj conn slots

        adj_conn_lengths = zeros(indices.shape, dtype=uint8)  # unsigned integer (0 to 255)
        for i, (index, row) in enumerate(zip(indices, arr)):
            if isnan(index):  # NaN means that there's no adj slots, so -> 0
                adj_conn_lengths[i] = 0

            index = int(index)
            # from the argmax index, walk to right to discover the rest of the adj conn size
            right_walk = sum(1 for _ in takewhile(lambda x: x == 0, row[self.fiber_slot + index:]))
            # from the argmax index, walk to left to discover the rest of the adj conn size
            left_walk = sum(1 for _ in takewhile(lambda x: x == 0, flip(row[:self.fiber_slot + index])))
            # total adj conn size will be the sum of left & right walks
            adj_conn_lengths[i] = right_walk + left_walk

        non_zero = nonzero(adj_conn_lengths)  # avoid div by 0
        reason = count_adjs[non_zero] / adj_conn_lengths[non_zero]
        in_xt = sum(reason)

        self.in_xt = in_xt  # ?
        return in_xt
