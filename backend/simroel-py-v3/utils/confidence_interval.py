from pandas import read_csv
from numpy import any


# TODO: testar os valores e comparar com o simroel-py-v3 por conta da mudanca de `i` e `j`
class ConfidenceInterval(object):
    def __init__(self,
                 confidence_interval_path,
                 ci,
                 n_simulations,
                 ):
        self.ci = ci
        self.n_sims = n_simulations
        self.data = read_csv(confidence_interval_path).set_index("index")

    def __repr__(self):
        return "<{}({})>".format(
            self.__class__.__name__,
            ", ".join("{}={!r}".format(k, v) for k, v in self.__dict__.items())
        )

    def get_interval(self):
        i, n_simulations = self.get_n_simulations()
        j, percentage = self.percentage()

        indices = {
            40: self.data.loc["31", j] if percentage else -1,
            60: self.data.loc["32", j] if percentage else -1,
            120: self.data.loc["33", j] if percentage else -1
        }

        if self.n_sims <= 30:
            return self.data.iloc[i, j] if (percentage and n_simulations) else -1

        return indices.get(self.n_sims, self.data.loc["34", j] if percentage else -1)

    # TODO: remover dependencia dessas funcoes
    def percentage(self):
        condition = self.data.columns == str(self.ci)
        percentage = any(condition)
        index = self.data.columns[condition][0] if percentage else self.data.columns[-1]
        return index, percentage

    def get_n_simulations(self):
        condition = self.data.index == str(self.n_sims)
        sims = any(condition)
        index = self.data.index[condition][0] if sims else self.data.index[-1]
        return index, sims
