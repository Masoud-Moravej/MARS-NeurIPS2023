from math import sqrt, log
from statistics import mean
from random import choices,sample

from IndexPolicy import IndexPolicy

class BESA(IndexPolicy):

    def __init__(self, nbArms):
        self.nbArms = nbArms
        self.nbDraws = dict()
        self.cumReward = dict()

        self.RR = {}
        self.UCBALL = {}


    def startGame(self):
        self.t = 1
        for arm in range(self.nbArms):
            self.nbDraws[arm] = 0
            self.cumReward[arm] = 0.0
            self.RR[arm] = [0]*2000
            self.UCBALL[arm] = 0

    def computeIndex(self, arm):
        if self.nbDraws[arm] == 0:
            return float('+infinity')
        else:
            return self.UCBALL[arm]

    def getReward(self, arm, reward):
        self.nbDraws[arm] += 1
        self.cumReward[arm] += reward
        self.t += 1

        self.RR[arm][self.nbDraws[arm]-1] = reward

        other_arm = int(1-arm)

        if self.nbDraws[other_arm] != 0:    
            if self.nbDraws[arm] > self.nbDraws[other_arm]:
                II = sample(self.RR[arm][0:self.nbDraws[arm]], k=self.nbDraws[other_arm])
            else:
                II = self.RR[arm][0:self.nbDraws[arm]]
            
            self.UCBALL[arm] = mean(II)

            if self.nbDraws[other_arm] > self.nbDraws[arm]:
                II = sample(self.RR[other_arm][0:self.nbDraws[other_arm]], k=self.nbDraws[arm])
            else:
                II = self.RR[other_arm][0:self.nbDraws[other_arm]]
            
            self.UCBALL[other_arm] = mean(II)
        else:
            self.UCBALL[arm] = float('+infinity')