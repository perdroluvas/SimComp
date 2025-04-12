# TODO

from numpy import (
    stack,
    expand_dims,
    all,
    argwhere
)
from numpy.random import choice
from numpy.lib.stride_tricks import as_strided

"""
https://towardsdatascience.com/fast-and-robust-sliding-window-vectorization-with-numpy-3ad950ed62f5
"""


class Assignment(object):
    def __init__(self, allocation_type):
        assert allocation_type in ("first_fit", "random_fit"), "Accepted allocation types: first_fit, random_fit"
        self.allocation_type = allocation_type

    @staticmethod
    def _get_strides(arr, window):
        shape = arr.shape[:-1] + (arr.shape[-1] - window + 1, window)
        strides = arr.strides + (arr.strides[-1],)
        return as_strided(arr, shape=shape, strides=strides)

    def get_slots(self, slots, guard_band, fiber, route, core):
        sample = stack([fiber.get(k)[core] for k in route])
        sample = expand_dims(sample, 0)
        strides = self._get_strides(sample, slots + guard_band)
        indices = argwhere(all(strides == -1, axis=(1, -1, 0))).reshape(-1,)

        if indices.size == 0:
            return -1

        if self.allocation_type == "first_fit":
            ff = indices[0]
            return ff, ff + slots + guard_band
        rf = choice(indices)
        return rf, rf + slots + guard_band

    def alloc(self, connection, fiber, route, core):

        free_slots = self.get_slots(int(connection.slots), connection.guard_band, fiber.fiber_data, route, core)

        if free_slots == -1:
            return False

        # set connection data
        connection.update(fiber_core=core, fiber_slot=free_slots[0], free_slots=free_slots, route=route)
        fiber.alloc(connection)

        return True
