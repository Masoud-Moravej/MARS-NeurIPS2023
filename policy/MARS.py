
import numpy as np

from math import sqrt, log

from IndexPolicy import IndexPolicy

class MARS(IndexPolicy):
    """Class that implements the MARS policy proposed in the paper"""

    def __init__(self, nbArms, amplitude=1., lower=0.):
        self.nbArms = nbArms
        self.amplitude = amplitude
        self.lower = lower
        self.nbDraws = {}
        self.cumReward = {}

        self.c = 1/1000
        self.RR = {}
        self.subsampleReward = {}
        self.UCBALL = {}



    def startGame(self):
        self.t = 1
        for arm in range(self.nbArms):
            self.nbDraws[arm] = 0
            self.cumReward[arm] = 0.0
            self.RR[arm] = [0]*2000
            self.subsampleReward[arm] = {}
            self.UCBALL[arm] = 0
            for i in range(2):
                self.subsampleReward[arm][i] = [0]*int(1/self.c)
            

    def computeIndex(self, arm):
        if self.nbDraws[arm] == 0:
            return float('+infinity')
        else:
            return self.UCBALL[arm]

    def getReward(self, arm, reward):
        self.nbDraws[arm] += 1
        self.cumReward[arm] += reward
        self.t += 1

        self.RR[arm][self.nbDraws[arm]] = reward

        for count in range(int(1/self.c)):
            if np.random.randint(low=1, high=3) == 2:
                self.subsampleReward[arm][0][count] = self.subsampleReward[arm][0][count] + 1
                self.subsampleReward[arm][1][count] =  (reward+(self.subsampleReward[arm][0][count]-1)*self.subsampleReward[arm][1][count])/(self.subsampleReward[arm][0][count])
        
        if self.nbDraws[arm]*log(2) < log(1/self.c):
            p = self.c*(2**(int(self.nbDraws[arm])))
            if 1-p > np.random.random(1)[0]:
                self.UCBALL[arm] = float('+infinity')
            elif p < 1:
                self.UCBALL[arm] = max(self.RR[arm])
        else:
            self.UCBALL[arm] = max(self.subsampleReward[arm][1])

