from Arm import Arm
from scipy.stats import truncnorm 

class TruncatedGaussian(Arm):
    def __init__(self, mu):
        self.mu = mu
        self.expectation = mu

        
    def draw(self):
        return self.mu + truncnorm.rvs(-1, 1,size = 1)[0]
