import random
import time

class Simulation(object):

	"""
	Initializes simulation with values set for the following variables:
	1. q0 --> The initial value for the mining power allocated.
	1. q  --> The ceiling for mining power allocated.
	2. z  --> The max number of blocks the merchant waits before handing over goods to the attacker. 
	3. d  --> The chance for either the attacker or the honest miner to find the block. 
	"""
	def __init__(self, q0, q, z, d):
		self.q0 = q0
		self.q  = q
		self.z  = z
		self.d  = d

	"""
	Checks if there is a winner during one run in the trial. Returns are as follows:
	0  --> Honest miner won
	1  --> Attacker won
	-1 --> There is no winner in this round
	"""
	def is_winner(self,q,z,d):
		miner_chance = random.randInt(1,d)
		attacker_chance = random.randInt(1,d)
		miner_q = random.seed(time.time())
		attacker_q = random.seed(time.time())
		if((attacker_q < q) and (attacker_chance == 1)):
			return 1
		elif((miner_q < (1-q)) and (miner_chance == 1)):
			return 0
		else:
			return -1

	"""
	Runs 180 events for each trial. Each independant event records the winners of each trial.
	All values are stored into a python dictionary in tuples denotes by z : (q, winner_val) 
	"""
	def run_trial(self):
		q = self.q0
		winners = {}
		for z in range(1, self.z):
			while (q <= self.q):
				if(self.is_winner(q, z, self.d) == 1):
					winners[z] = (q, 1)
					q += .02
				elif(self.is_winner(q, z, self.d) == 0):
					winners[z] = (q, 0)
					q += .02
				else:
					continue
		return winners





