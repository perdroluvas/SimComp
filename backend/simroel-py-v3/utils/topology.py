# TODO

from networkx import (
    DiGraph
)
from collections import namedtuple
from fiber import Fiber
from crosstalk.crosstalk_main import CrosstalkMain


class Topology(object):
    def __init__(self, topology_info):
        self.topology_info = topology_info
        self.EdgeData = namedtuple("EdgeData", ["fiber", "crosstalk"])

    def _create_topology(self):
        pass
