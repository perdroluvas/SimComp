from osnr.osnr_utils import OSNRUtils
from routing.router import Router
import numpy as np
from auxiliar.functions import (
    db_to_linear,
    linear_to_db,
    f_name,
    valid_division,
)
from auxiliar.constants import (
    MARGIN,
    CROSS_IMPEDANCE,
    OSNR_NLI_GAMMA,
    OSNR_NLI_BETA2
)



class OSNR(object):
    def __init__(self,
                 lamb,
                 amplifier_noise,
                 b_ref,
                 span_length,
                 node_loss,
                 limit_single_carrier,
                 router: Router,
                 osnr_utils: OSNRUtils):

        self.router = router
        self.osnr_utils = osnr_utils
        self.lamb = lamb
        self.fn = db_to_linear(amplifier_noise)
        self.b_ref = b_ref * np.power(10, 9)
        self.l_span = span_length
        self.l_no = db_to_linear(node_loss)
        self.limit_single_carrier = limit_single_carrier
        self.ase = {}

    def calculate_ase(self, route, source, target, k):
        name = f_name(source, target, k)

        if name in self.ase:
            return self.ase[name]


        weights = np.array(self.router.calc_weight(route))
        n_amp = np.ceil(weights / self.l_span).sum().astype(int)

        remaining = np.modf(weights / self.l_span)[0] * (self.l_span * self.lamb)
        remaining = remaining[remaining != 0]

        G = np.full((n_amp,), self.l_span * self.lamb)
        G[:len(remaining)] = remaining
        g = db_to_linear(G)

        """ 1.28545737824e-19 = H (Planck's constant) * V (optical channel carrier frequency)
        H = 6.62606896e-34  # J/Hz
        V = 1.94e14  # Hz
        """
        s_ase = (self.fn / 2.0) * ((g - 1.0) * 1.28545737824e-19)
        s_ase = np.hstack([s_ase, np.repeat((self.fn / 2.0) * ((self.l_no - 1.0) * 1.28545737824e-19),
                                            weights.shape[0])])
        s_ase_tot = np.sum(s_ase)
        self.ase[name] = s_ase_tot

        return s_ase_tot

    def calculate_nli(self, route, connection, fiber, power):
        total_adjacent = dict()

        for link in route:
            adj_info = self.osnr_utils.count_adj_connections(fiber[link][connection.fiber_core], connection, link)
            total_adjacent.update(adj_info)

        sum_gnli = 0
        f_i = connection.fiber_slot + (connection.slots / 2)
        b_i = connection.slots * self.b_ref
        ro = (np.square(np.pi) * np.abs(OSNR_NLI_BETA2)) / self.lamb
        mu = (3 * np.square(OSNR_NLI_GAMMA) * np.power(power, 3)) / (2 * np.pi * self.lamb * np.abs(OSNR_NLI_BETA2))

        for link, info in total_adjacent.items():
            conn_sizes = np.array([data[0] for data in info])
            conn_ini = np.array([data[1] for data in info])

            b_j = conn_sizes * self.b_ref
            f_j = conn_ini + (conn_sizes / 2)
            delta = np.abs(f_i - f_j) * self.b_ref
            num = delta + (b_j / 2)
            den = delta - (b_j / 2)
            sum_j = np.log(valid_division(num, den)).sum()
            #sum_j = np.log( (delta + (b_j / 2)) / (delta - (b_j / 2)) ).sum()

            link_gnli_aux = mu * (np.log(ro * np.square(b_i)) + sum_j)
            dist = self.router.calc_weight([link])[0]
            link_spans = dist // self.l_span
            sum_gnli = link_spans * link_gnli_aux

        return sum_gnli

    def validate(self, route, connection, fiber, k, validation="osnr"):
        #assert validation in ("osnr", "nli"), "Validation must be 'osnr' or 'nli'."

        osnr_req = self.osnr_utils.get_osnr_required(connection.size, connection.modulation)
        s_ase_tot = self.calculate_ase(route, connection.src, connection.tgt, k)

        if validation == "osnr":
            osnr_result = connection.power / (2 * s_ase_tot * self.b_ref)

        if validation == "nli" or "estrategia" in validation:
            sum_nli = self.calculate_nli(route, connection, fiber, connection.power)
            osnr_result = connection.power / ((2 * s_ase_tot * self.b_ref) + sum_nli)

            if validation == "estrategia_1":
                return linear_to_db(osnr_result)

        return linear_to_db(osnr_result) >= (osnr_req )#+ MARGIN + CROSS_IMPEDANCE)