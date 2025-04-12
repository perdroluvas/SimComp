# simulate_and_summarize.py

import json
from simulation import Simulation

def load_parameters(erlang):
    with open('../data/parameters.json', 'r+') as f:
        data = json.load(f)
        data['traffic_lambda'] = 1/erlang # <--- add id value.
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

def simulate_and_summarize(simu, erlang, n_total):
    # Call the function that loads the parameters
    load_parameters(erlang)

    sim = Simulation()
    sim.simulate(simu, n_total)
    sim.stats.summarize()
    return sim.stats.results()
