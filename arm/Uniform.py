from Arm import Arm
import numpy as np 

class Uniform(Arm):
    def __init__(self, mu):
        self.mu = mu
        self.expectation = mu

        
    def draw(self):
        return self.mu + np.random.uniform(-1,1,1)[0]
