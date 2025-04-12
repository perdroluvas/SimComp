import pandas as pd
import os
import json
import time
import multiprocessing as mp
from simulation import Simulation

def process_element(element):
    simu = 1
    total = pd.DataFrame()
    erlang = element
    with open('../data/parameters.json', 'r+') as f:
        data = json.load(f)
        data['traffic_lambda'] = 1/erlang # <--- add id value.
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
    for i in range(n_repeat):
        sim = Simulation()
        sim.simulate(simu, n_total)
        sim.stats.summarize()
        results = sim.stats.results()
        results['Load'] = erlang
        total = pd.concat([total, results])
        simu+=1
    return total

inicio = time.time()
total = pd.DataFrame()
loads = [400, 500, 600, 700, 800, 900, 1000]
n_repeat = 2
n_total = len(loads)*n_repeat

# Cria um pool de 4 processos
with mp.Pool(16) as p:
    results_list = p.map(process_element, loads)

# Concatena os resultados de cada processo
for results in results_list:
    total = pd.concat([total, results])

path = os.getcwd()
path = path.split(os.sep)[:-1]
path = os.sep.join(path)
path = path + os.sep+'Result'
print(total)
total.to_csv(path + os.sep +'results_simulation.csv', index=False)

fim = time.time()
print(fim - inicio)


