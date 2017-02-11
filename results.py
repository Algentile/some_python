import csv
import random
import time
from simulation import Simulation

def write_to_csv(key, dict):
	with open("results.{}.csv".format(key), 'a') as output:
		writer = csv.writer(output)
		writer.writerow(["q", "z", "test"])
		for k,v in dict.iteritems():
			for item in v:
				(q,test) = item
				writer.writerow([q, z, test])

if __name__ == "__main__":
	for i in range(1,2):
		sim = Simulation(.040, .4, 10, 100)
		results = sim.run_trial()
		write_to_csv(random.seed(time.time()), results)


