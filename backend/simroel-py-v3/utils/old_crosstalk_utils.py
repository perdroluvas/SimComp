from files.properties import Properties
import pandas as pd


class CrosstalkUtils:
    def __init__(self):
        self.parameters = Properties()
        self.ber_type = self.parameters.get_ber_type()
        self.xt_req = self._handle_xt_req()

    def _handle_xt_req(self):
        xt_dict = self.parameters.fm.dict_crosstalk
        return pd.read_csv(xt_dict[self.ber_type], index_col="modulation")

    def get_xt_req(self, conn_size, modulation):
        conn_size = str(float(conn_size))
        modulation = int(modulation.split("-")[0])
        assert (conn_size in self.xt_req.columns), f"[XT] Invalid conn_type for this BER ({self.ber_type})"
        assert (modulation in self.xt_req.index), f"[XT] Invalid modulation for this BER ({self.ber_type})"

        return self.xt_req.loc[modulation, conn_size]