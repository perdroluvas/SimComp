import os
import glob
import json


def get_files(directory, extension=".txt"):
    """
    Return a list of absolute paths to all files in `directory` with the given extension.
    e.g., if extension == ".txt", we grab all *.txt in that directory.
    Uses `glob` so it works cross-platform.
    """
    pattern = os.path.join(directory, f"*{extension}")
    return glob.glob(pattern)


def structure(directory, extension=".txt"):
    """
    Return a dictionary mapping each file's name (without extension)
    to its absolute path. Example:
    {
       "ber_1-1": "/full/path/to/ber_1-1.txt",
       "ber_1-5": "/full/path/to/ber_1-5.txt",
       ...
    }
    """
    result = {}
    paths = get_files(directory, extension)
    for p in paths:
        base = os.path.basename(p)                   # e.g., "ber_1-1.txt"
        key = os.path.splitext(base)[0]              # e.g., "ber_1-1"
        result[key] = os.path.abspath(p)             # store the absolute path
    return result


class FileManager(object):
    def __init__(self):
        # Get absolute path to current working directory
        abs_path = os.path.abspath(os.getcwd())
        
        # Locate your project root up to "simroel-py-v3"
        marker = "simroel-py-v3"
        if marker in abs_path:
            # We'll truncate at the end of "simroel-py-v3"
            base_idx = abs_path.find(marker) + len(marker)
            # Now abs_path is the path up to ".../simroel-py-v3"
            abs_path = abs_path[:base_idx]
        
        # Build the standard data directories (cross-platform)
        self.data_dir = os.path.join(abs_path, "data")
        self.topologies_dir = os.path.join(self.data_dir, "topologies")
        self.osnr_dir = os.path.join(self.data_dir, "osnr")
        self.crosstalk_dir = os.path.join(self.data_dir, "crosstalk")

        # Example paths for JSON, CSV files, etc.
        self.parameters_path = os.path.join(self.data_dir, "parameters.json")
        self.confidence_interval_path = os.path.join(self.data_dir, "confidence_interval.csv")
        self.traffic_input_file_path = os.path.join(self.data_dir, "traffic_input_file.csv")

        # If you specifically want a relative path for parameters.json, do so carefully:
        # self.parameters_path = "../parameters.json"  # Overriding if needed

        # Build the dictionaries for text files
        self.dict_topologies = structure(self.topologies_dir, ".txt")
        self.dict_osnr = structure(self.osnr_dir, ".txt")
        self.dict_crosstalk = structure(self.crosstalk_dir, ".txt")
    def create_default_params(self):
        # Cria um default, não sei se valeria a pena mas está aqui um esqueleto.
        default_params = {"slot_size": 12.5}  # Default initial value
        with open(self.parameters_path, "w") as f:
            json.dump(default_params, f, indent=4)

    def get_params(self):
        # print(self.parameters_path)
        with open(self.parameters_path, "r") as f:
            properties = json.load(f)
        return properties
    ###TODO Tentativas de escrever no parameters.json
    def save_params(self, params):
        try:
            with open(self.parameters_path, "w") as f:
                json.dump(params, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving parameters: {e}")
            return False

    def set_slot_size(self, slot_size):
        try:
            params = self.get_params()
            params["slot_size"] = slot_size
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting slot size: {e}")
            return False
    def set_core_pitch(self, core_pitch):
        try:
            params = self.get_params()
            params["core_pitch"] = core_pitch
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting core pitch: {e}")
            return False
    def set_bandwidth(self, bandwidth):
        try:
            params = self.get_params()
            params["bandwidth"] = bandwidth
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting bandwidth: {e}")
            return False

    def set_node_loss(self, node_loss):
        try:
            params = self.get_params()
            params["node_loss"] = node_loss
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting node loss: {e}")
            return False

    # Method for setting fiber_loss_coefficient
    def set_fiber_loss_coefficient(self, fiber_loss_coefficient):
        try:
            params = self.get_params()
            params["fiber_loss_coefficient"] = fiber_loss_coefficient
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting fiber loss coefficient: {e}")
            return False

    # Method for setting noise_figure
    def set_noise_figure(self, noise_figure):
        try:
            params = self.get_params()
            params["noise_figure"] = noise_figure
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting noise figure: {e}")
            return False

    def set_traffic_input_file(self, traffic_input_file):
        try:
            params = self.get_params()
            params["traffic_input_file"] = traffic_input_file
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting traffic input file: {e}")
            return False

    def set_n_connections(self, n_connections):
        try:
            params = self.get_params()
            params["n_connections"] = n_connections
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting number of connections: {e}")
            return False

    def set_n_simulations(self, n_simulations):
        try:
            params = self.get_params()
            params["n_simulations"] = n_simulations
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting number of simulations: {e}")
            return False

    def set_traffic_lambda(self, traffic_lambda):
        try:
            params = self.get_params()
            params["traffic_lambda"] = traffic_lambda
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting traffic lambda: {e}")
            return False

    def set_traffic_refresh(self, traffic_refresh):
        try:
            params = self.get_params()
            params["traffic_refresh"] = traffic_refresh
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting traffic refresh: {e}")
            return False

    def set_traffic_file(self, traffic_file):
        try:
            params = self.get_params()
            params["traffic_file"] = traffic_file
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting traffic file: {e}")
            return False

    def set_traffic_conn_types(self, traffic_conn_types):
        try:
            params = self.get_params()
            params["traffic_conn_types"] = traffic_conn_types
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting traffic connection types: {e}")
            return False

    def set_route_algorithm(self, route_algorithm):
        try:
            params = self.get_params()
            params["route_algorithm"] = route_algorithm
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting route algorithm: {e}")
            return False

    def set_k_routes(self, k_routes):
        try:
            params = self.get_params()
            params["k_routes"] = k_routes
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting k routes: {e}")
            return False

    def set_route_selection(self, route_selection):
        try:
            params = self.get_params()
            params["route_selection"] = route_selection
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting route selection: {e}")
            return False

    def set_pcc_holding_time(self, pcc_holding_time):
        try:
            params = self.get_params()
            params["pcc_holding_time"] = pcc_holding_time
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting PCC holding time: {e}")
            return False

    def set_guard_band(self, guard_band):
        try:
            params = self.get_params()
            params["guard_band"] = guard_band
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting guard band: {e}")
            return False

    def set_conn_holding_time(self, conn_holding_time):
        try:
            params = self.get_params()
            params["connection_holding_time"] = conn_holding_time
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting connection holding time: {e}")
            return False

    def set_tracer(self, tracer):
        try:
            params = self.get_params()
            params["tracer"] = tracer
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting tracer: {e}")
            return False

    def set_osnr(self, osnr):
        try:
            params = self.get_params()
            params["osnr"] = osnr
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting OSNR: {e}")
            return False

    def set_modulation(self, modulation):
        try:
            params = self.get_params()
            params["modulation"] = modulation
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting modulation: {e}")
            return False

    def set_lambda(self, lambda_value):
        try:
            params = self.get_params()
            params["lambda"] = lambda_value
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting lambda: {e}")
            return False

    def set_fn(self, fn):
        try:
            params = self.get_params()
            params["fn"] = fn
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting fn: {e}")
            return False

    def set_p(self, p):
        try:
            params = self.get_params()
            params["p"] = p
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting p: {e}")
            return False

    def set_span_length(self, span_length):
        try:
            params = self.get_params()
            params["span_length"] = span_length
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting span length: {e}")
            return False

    def set_band_ref(self, band_ref):
        try:
            params = self.get_params()
            params["bandwidth_reference"] = band_ref
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting bandwidth reference: {e}")
            return False

    def set_limit_single_carrier(self, limit_single_carrier):
        try:
            params = self.get_params()
            params["limit_single_carrier"] = limit_single_carrier
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting limit single carrier: {e}")
            return False

    def set_wavelength(self, wavelength):
        try:
            params = self.get_params()
            params["wavelength"] = wavelength
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting wavelength: {e}")
            return False

    def set_bending_radius(self, bending_radius):
        try:
            params = self.get_params()
            params["bending_radius"] = bending_radius
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting bending radius: {e}")
            return False

    def set_coupling_coeff(self, coupling_coeff):
        try:
            params = self.get_params()
            params["coupling_coeff"] = coupling_coeff
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting coupling coefficient: {e}")
            return False

   # def set_core_pitch(self, core_pitch):
    #    try:
     #       params = self.get_params()
      #      params["core_pitch"] = core_pitch
       #     return self.save_params(params)
        #except Exception as e:
         #   print(f"Error setting core pitch: {e}")
          #  return False

    def set_confidence_interval(self, confidence_interval):
        try:
            params = self.get_params()
            params["ci"] = confidence_interval
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting confidence interval: {e}")
            return False

    def set_thread_number(self, thread_number):
        try:
            params = self.get_params()
            params["thread_number"] = thread_number
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting thread number: {e}")
            return False

    def set_pcc_time_threshold(self, pcc_time_threshold):
        try:
            params = self.get_params()
            params["pcc_time_threshold"] = pcc_time_threshold
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting PCC time threshold: {e}")
            return False
