import random as rand
from Arm import Arm

class Gaussian(Arm):
    def __init__(self, mu, sigma):
        self.sigma = sigma
        self.mu=mu
        self.expectation = mu
        
    def draw(self):
        return self.mu+self.sigma*rand.gauss(0,1)
