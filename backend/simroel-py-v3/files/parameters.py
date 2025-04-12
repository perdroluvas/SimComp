from numpy import (
    int64 as int_, # ou int_
    float64 as float_, #ou float_
    loadtxt,
    arange,
    array
)
from pandas import (
    DataFrame,
    read_csv,
    to_numeric
)
from networkx import (
    from_pandas_edgelist,
    get_edge_attributes,
    DiGraph
)
import json as json

from auxiliar.constants import MCF_CONFIGS
from auxiliar.functions import CORE_SELECTION_FN
from files.file_manager import FileManager


class Params(object):
    def __init__(self):
        self.file_manager = FileManager()
        self.topologies = self.file_manager.dict_topologies
        self.params = self.file_manager.get_params()


    def get_mcf_config(self):
        assert self.params["n_cores"] in [2, 7, 12, 19, 22, 30]
        return MCF_CONFIGS[self.params["n_cores"]]

    def get_file_topology(self):
        assert self.topologies.__contains__(self.params["file_topology"]), "Invalid topology."
        return self.params["file_topology"]

    def get_xt_table(self):
        xt_dict = self.file_manager.dict_crosstalk
        df_xt = read_csv(xt_dict[self.get_ber_type()], index_col="modulation")
        df_xt.columns = to_numeric(df_xt.columns)
        return df_xt

    def get_osnr_table(self):
        osnr_table = self.file_manager.dict_osnr
        df_osnr = read_csv(osnr_table[self.get_ber_type()], index_col="modulation")
        df_osnr.columns = to_numeric(df_osnr.columns)
        return df_osnr

    def get_topology_info(self):
        raw_topology = loadtxt(self.topologies[self.get_file_topology()], delimiter=";")
        topology = DataFrame(raw_topology, columns=["source", "target", "weight"])
        topology[["source", "target"]] = topology[["source", "target"]].astype(int) - 1
        graph = from_pandas_edgelist(topology, source="source", target="target", edge_attr=True, create_using=DiGraph)

        nodes = int_(graph.nodes)
        edges, weights = zip(*get_edge_attributes(graph, "weight").items())
        weights = float_(weights)[None, :]
        return {"graph": graph, "edges": edges, "weights": weights, "nodes": nodes}

    def get_traffic_input_file(self):
        return self.params.traffic_input_file

    def get_n_connections(self):
        assert isinstance(self.params["n_connections"], int)
        return self.params["n_connections"]

    def get_n_simulations(self):
        assert isinstance(self.params["n_simulations"], int)
        return self.params["n_simulations"]

    def load_params(self):
        # Load the parameters from the JSON file
        with open(self.params, 'r') as file:
            return json.load(file)

    def set_slot_size(self, slot_size: float):
        # Set the slot size and save the parameters
        self.params["slot_size"] = slot_size
        self.params.save_params()

    def get_slot_size(self):
        # Make sure the slot size is not a string and return it
        assert not isinstance(self.params["slot_size"], str)
        return self.params["slot_size"]

    def get_n_cores(self):
        assert isinstance(self.params["n_cores"], int)
        return self.params["n_cores"]

    def get_cores(self):
        return arange(self.get_n_cores())

    def get_allocation_type(self):
        """fiber and core"""
        return self.params["allocation"]

    def get_allocation_fn(self):
        return CORE_SELECTION_FN[self.get_allocation_type()]

    def get_node_loss(self):
        assert isinstance(self.params["node_loss"], float) #verificara se não muda a simulação
        return self.params["node_loss"]

    def set_node_loss(self):
        assert not isinstance(self.params["node_loss"], float)
        return self.params["node_loss"]

    def get_fiber_loss_coefficient(self):
        assert isinstance(self.params["fiber_loss_coefficient"], int)
        return self.params["fiber_loss_coefficient"]

    def set_fiber_loss_coefficient(self):
        assert not isinstance(self.params["fiber_loss_coefficient"], float)
        return self.params["fiber_loss_coefficient"]

    def get_noise_figure(self):
        assert isinstance(self.params["noise_figure"], int)
        return self.params["noise_figure"]

    def set_noise_figure(self):
        assert not isinstance(self.params["noise_figure"], float)
        return self.params["noise_figure"]

    def set_bandwidth(self):
        assert not isinstance(self.params["bandwidth"], str)
        return self.params["bandwidth"]

    def get_bandwidth(self):
        assert isinstance(self.params["bandwidth"], int)
        return self.params["bandwidth"]

    def get_traffic_lambda(self):
        return array(self.params["traffic_lambda"])

    def get_traffic_refresh(self):
        assert isinstance(self.params["traffic_refresh"], bool)
        return self.params["traffic_refresh"]

    def get_traffic_file(self):
        assert isinstance(self.params["traffic_file"], bool)
        return self.params["traffic_file"]

    def get_traffic_conn_types(self):
        return array(self.params["traffic_conn_types"])

    def get_route_algorithm(self):
        assert isinstance(self.params["route_algorithm"], str)
        return self.params["route_algorithm"]

    def get_k_routes(self):
        assert isinstance(self.params["k_routes"], int)
        return self.params["k_routes"]

    def get_route_selection(self):
        assert isinstance(self.params["route_selection"], str)
        return self.params["route_selection"]

    def get_pcc_holding_time(self):
        assert isinstance(self.params["pcc_holding_time"], int)
        return self.params["pcc_holding_time"]

    def get_guard_band(self):
        assert type(self.params["guard_band"]) is int, "`guard_band` type must be int"
        return self.params["guard_band"]

    def get_conn_holding_time(self):
        return self.params["connection_holding_time"]

    def get_tracer(self):
        return self.params["tracer"]

    def get_osnr(self):
        return self.params["osnr"]

    def get_modulation(self):
        return self.params["modulation"]

    def get_lambda(self):
        return self.params["lambda"]

    def get_fn(self):
        return self.params["fn"]

    def get_p(self):
        return self.params["p"]

    def get_span_length(self):
        return self.params["span_length"]



    def get_band_ref(self):
        return self.params["bandwidth_reference"]

    def get_limit_single_carrier(self):
        assert isinstance(self.params["limit_single_carrier"], int)
        return self.params["limit_single_carrier"]

    def get_wavelength(self):
        return self.params["wavelength"]

    def get_bending_radius(self):
        return self.params["bending_radius"]

    def get_coupling_coeff(self):
        return self.params["coupling_coeff"]

    def set_core_pitch(self, core_pitch: float):
        # Set the slot size and save the parameters
        self.params["core_pitch"] = core_pitch
        self.params.save_params()

    def get_core_pitch(self):
        assert not isinstance(self.params["core_pitch"], str)
        return self.params["core_pitch"]

    def get_port_isolation(self):
        return self.params["port_isolation"]

    def get_crosstalk_reason(self):
        return self.params["crosstalk_reason"]

    def get_calculate_crosstalk(self):
        return self.params["calculate_crosstalk"]

    def get_confidence_interval(self):
        return self.params["ci"]

    def get_thread_number(self):
        return self.params["thread_number"]

    def get_pcc_time_threshold(self):
        return self.params["pcc_time_threshold"]

    def get_ber_type(self):
        assert self.params["osnr_ber_type"] in self.file_manager.dict_osnr.keys(), \
            f"BER must Be in {self.file_manager.dict_osnr.keys()}"
        return self.params["osnr_ber_type"]
