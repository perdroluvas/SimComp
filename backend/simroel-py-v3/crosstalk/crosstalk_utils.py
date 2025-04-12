from pandas import DataFrame


class CrosstalkUtils(object):
    def __init__(self, cross_required_table: DataFrame):
        self.cross_required_table = cross_required_table

    def get_cross_required(self, conn_size, modulation):
        assert (conn_size in self.cross_required_table.columns), \
            f"[XT] Invalid `conn_type` for this BER"
        assert (modulation in self.cross_required_table.index), \
            f"[XT] Invalid `modulation` for this BER"

        return self.cross_required_table.loc[modulation, conn_size]
