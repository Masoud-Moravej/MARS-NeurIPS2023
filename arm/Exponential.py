from random import random
from math import isinf,exp,log

from Arm import Arm

class Exponential(Arm):
	def __init__(self, p, trunc = float('inf')):
		self.p = p
		self.trunc = trunc
		if isinf(trunc):
			self.expectation = 1./p
		else:
			self.expectation = (1.-exp(-p * trunc)) / p
				
	def draw(self):
		return min(-1./self.p*log(random()), self.trunc)
