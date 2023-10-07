from Posterior import Posterior
from math import sqrt
import numpy as np

from random import betavariate
from scipy.special import btdtri

class GaussianVar1(Posterior):

    def __init__(self):

        self.N = 0
        self.S = 0
        
    def reset(self):
        self.N = 0 
        self.S = 0 

    def update(self, obs):
        self.N = self.N + 1
        self.S = self.S + obs
            
        
    def sample(self):
        if self.N ==0:
            return float('+infinity')
        
        std = sqrt(1)

        return sqrt(1/(self.N))*np.random.normal(0, std)+ self.S/self.N
            