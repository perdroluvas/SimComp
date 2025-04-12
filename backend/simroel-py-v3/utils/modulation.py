from numpy import (
    ceil,
    log10
)
from auxiliar.constants import SPECTRAL_EFFS


class Modulation(object):
    def __init__(self,
                 guard_band,
                 slot_size,
                 modulations,
                 lim_single_carrier,
                 ):
        self.guard_band = guard_band
        self.slot_size = slot_size
        self.modulations = modulations
        self.lim_single_carrier = lim_single_carrier
        self.spectral_eff = 0.0
        self.b_super_channel = dict(zip(self.modulations, [0.0, 0.0, 0.081, 0.045, 0.0]))

    def calculate_n_slots(self, modulation, conn):
        eff = SPECTRAL_EFFS.get(modulation, 2)
        self.spectral_eff = 2 * (log10(eff) / log10(2))

        if conn.size <= self.lim_single_carrier:
            return self.single_carrier(conn)
        return int(self.super_channel(modulation, conn))

    def single_carrier(self, conn):
        slots = ceil(conn.size / (self.slot_size * self.spectral_eff))
        return slots + self.guard_band

    def super_channel(self, modulation, conn):
        nsc = ceil(conn.size / self.lim_single_carrier)
        rs = self.lim_single_carrier / self.spectral_eff
        size = ((nsc - 1) * (1 + self.b_super_channel.get(modulation)) + 1) * rs
        slots = ceil(size / self.slot_size)
        return slots + self.guard_band
