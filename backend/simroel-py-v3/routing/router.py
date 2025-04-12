import networkx as nx
from itertools import islice
from numpy import array

class Router:
    def __init__(self, topology_graph):
        self.graph = topology_graph
        self._edges = {(source, target): weight["weight"] for (source, target, weight) in self.graph.edges(data=True)}
        self.learned_paths = {}

    @staticmethod
    def _format_name(source, target, k):
        return f"s{source}t{target}k{k}"

    @staticmethod
    def _convert(routes):
        return [[(paths[i], paths[i+1]) for i in range(len(paths)-1)] for paths in routes]

    def shortest_paths(self, source, target, weight='weight', k=3):
        path_name = self._format_name(source, target, k)

        if path_name in self.learned_paths:
            return self.learned_paths[path_name]

        shortest_paths = nx.shortest_simple_paths(self.graph, source, target, weight)
        self.learned_paths[path_name] = self._convert(list(islice(shortest_paths, k)))
        return self.learned_paths[path_name]

    def calc_total_weight(self, routes):
        return sum(map(self.calc_weight, routes))

    def calc_weight(self, route):

        return array([self._edges.get(r) for r in route])

    def get_edges(self):
        return self.graph.edges
