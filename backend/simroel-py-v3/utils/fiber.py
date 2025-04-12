from numpy import (
    ceil,
    full,
    int8
)
from auxiliar.constants import (
    FREE_SLOT,
    GUARD_BAND,
    ALLOCATED
)


class Fiber(object):
    def __init__(self,
                 cores: int,
                 slot_size: float,
                 bandwidth: float,
                 src_tgt: dict
                 ):
        self.cores = cores
        self.slot_size = slot_size
        self.bandwidth = bandwidth
        self.n_slots = ceil(self.bandwidth / self.slot_size).astype(int)

        data = [full((self.cores, self.n_slots), FREE_SLOT) for _ in range(len(src_tgt))]
        self.fiber_data = dict(zip(src_tgt, data))

    def __repr__(self):
        return "<{}({})>".format(
            self.__class__.__name__,
            ", ".join("{}={!r}".format(k, v) for k, v in self.__dict__.items())
        )

    def alloc(self, connection):

        for link in connection.route:
            self.fiber_data.get(link)[connection.fiber_core, connection.free_slots[0]:connection.free_slots[1]] = connection.iid
            self.fiber_data.get(link)[connection.fiber_core, connection.free_slots[1] - 1] = GUARD_BAND

        return

    def free(self, connection):
        for link in connection.route:
            self.fiber_data.get(link)[connection.fiber_core, connection.free_slots[0]:connection.free_slots[1]] = FREE_SLOT
        return
