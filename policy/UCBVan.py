from math import sqrt, log

from IndexPolicy import IndexPolicy

class UCBVan(IndexPolicy):


    def __init__(self, nbArms, variance ,amplitude=1., lower=0.):
        self.nbArms = nbArms
        self.amplitude = amplitude
        self.lower = lower
        self.nbDraws = dict()
        self.cumReward = dict()
        self.variance = variance
        self.c = self.variance * 2


    def startGame(self):
        self.t = 1
        for arm in range(self.nbArms):
            self.nbDraws[arm] = 0
            self.cumReward[arm] = 0.0

    def computeIndex(self, arm):
        if self.nbDraws[arm] == 0:
            return float('+infinity')
        else:
            m = self.cumReward[arm]/self.nbDraws[arm] 
            return m + sqrt(self.c*log(1000)/self.nbDraws[arm])

    def getReward(self, arm, reward):
        self.nbDraws[arm] += 1
        self.cumReward[arm] += reward
        self.t += 1
