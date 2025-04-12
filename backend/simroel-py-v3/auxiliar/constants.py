from data.fiber_config.mcf_config import (
    MCF_2,
    MCF_7,
    MCF_12,
    MCF_19,
    MCF_22,
    MCF_30
)

FREE_SLOT = -1
GUARD_BAND = -2
ALLOCATED = 0

PROPAGATION_CONSTANT = 1e7
MARGIN = 3.
CROSS_IMPEDANCE = 1.
OSNR_NLI_GAMMA = 1.3
OSNR_NLI_BETA2 = -0.00213  # -2.13 / 1000 [-2.13/km]

SPECTRAL_EFFS = {
    "4-QAM": 4,
    "8-QAM": 8,
    "16-QAM": 16,
    "32-QAM": 32,
    "64-QAM": 64
}
MCF_CONFIGS = {
    2: MCF_2,
    7: MCF_7,
    12: MCF_12,
    19: MCF_19,
    22: MCF_22,
    30: MCF_30,
}
