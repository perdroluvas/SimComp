import pandas as pd
import os
from simulation import Simulation
import json
import time


total = pd.DataFrame()
# loads = [60, 100, 140, 180, 220, 260]
loads = [600, 800, 1000, 1200, 1400] #transformar isso em parametro
n_repeat = 2
n_total = len(loads)*n_repeat
simu = 1
for erlang in loads:
    with open('/home/pedrolucas/Documentos/GitHub/simroelfix/simroel-py-v3/parameters.json', 'r+') as f: #mudar diretorio de maneira exata
        data = json.load(f)
        data['traffic_lambda'] = 1/erlang # <--- add id value.
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

    for i in range(n_repeat):
        inicio = time.time()
        sim = Simulation()
        sim.simulate(simu, n_total)
        sim.stats.summarize()
        results = sim.stats.results()
        results['Load'] = erlang
        total = pd.concat([total, results])
        simu += 1
        fim = time.time()
        print(fim - inicio)
path = os.getcwd()
path = path.split(os.sep)[:-1]
path = os.sep.join(path)
path = path + os.sep+'Result'
print(total)
total.to_csv(path + os.sep + 'new_FF_est2.csv', index=False)


# import cProfile, pstats, io
# from pstats import SortKey
# pr = cProfile.Profile()
# pr.enable()
# sim = Simulation()
# sim.simulate(1, 1)
# pr.disable()
# s = io.StringIO()
# sortby = SortKey.CUMULATIVE
# ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
# ps.print_stats()
# print(s.getvalue())
# sim.stats.summarize()