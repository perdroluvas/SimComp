from numpy import (
    power,
    log10,
    r_,
    divide,
    ones_like,
    where
)

from random import sample
from glob import glob
import seaborn as sns
import matplotlib.pyplot as plt
# import warnings
# warnings.filterwarnings("error")

CORE_SELECTION_FN = {
    "first_fit": lambda cores: r_[cores[1:], cores[0]],
    "random_fit": lambda cores: sample(cores.tolist(), len(cores))
}


def structure(directory, extension):
    paths = glob(directory + "\\*" + extension)
    elements = list(map(lambda path: path.split("\\")[-1].replace(extension, ""), paths))
    return dict(zip(elements, paths))


def get_files(directory, extension="\\*.txt"):
    return glob(directory + extension)


def db_to_linear(x):
    return power(10, x / 10)


def linear_to_db(x):
    return 10 * log10(where(x != 0, x, 1))



def f_name(source, target, k):
    return f"s{source}t{target}k{k}"


def valid_division(num, den):
    return divide(num, den, out=ones_like(num), where=(den!=0))


def plot_xt_table(xt_table):
    sns.heatmap(xt_table, annot=True, fmt="g", cmap="viridis")
    plt.show()
