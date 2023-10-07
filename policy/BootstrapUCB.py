from math import sqrt, log
import numpy as np
import pandas as pd

from IndexPolicy import IndexPolicy

class BootstrapUCB(IndexPolicy):

    def __init__(self, nbArms):
        self.nbArms = nbArms
        self.nbDraws = dict()
        self.cumReward = dict()
        
        self.delta = 0.1
        self.rwd = np.zeros([self.nbArms, 2000])
        self.reg = np.zeros(2000)   
        self.count = np.zeros(self.nbArms)
        self.B = 200
        self.sample_mean = np.zeros(self.nbArms)
        self.error = np.zeros([self.nbArms, self.B])
        self.beta = np.zeros(self.nbArms)
        self.main = np.zeros(self.nbArms)
        self.remainder = np.zeros(self.nbArms)



    def startGame(self):
        self.t = 1
        for arm in range(self.nbArms):
            self.nbDraws[arm] = 0
            self.cumReward[arm] = 0.0
        
        self.delta = 0.1
        self.rwd = np.zeros([self.nbArms, 2000])
        self.reg = np.zeros(2000)   
        self.count = np.zeros(self.nbArms)
        self.B = 200 
        self.sample_mean = np.zeros(self.nbArms)
        self.error = np.zeros([self.nbArms, self.B])
        self.beta = np.zeros(self.nbArms)
        self.main = np.zeros(self.nbArms)
        self.remainder = np.zeros(self.nbArms)

    def computeIndex(self, arm):
        if self.nbDraws[arm] == 0:
            return float('+infinity')
        else:
            alpha_0 = 1/(1+self.t)
            self.sample_mean[arm] = np.mean(self.rwd[arm, :int(self.count[arm])])
            residual = self.rwd[arm, :int(self.count[arm])] - self.sample_mean[arm]
            
            for b in np.arange(self.B):
                self.error[arm, b] = sum(np.random.choice([-1,1], size = int(self.count[arm])) * residual) / int(self.count[arm]) 

            self.main[arm] = pd.DataFrame(self.error[arm, ]).quantile(1 - (alpha_0 * (1 - self.delta)))
            self.remainder[arm] = ((2 * np.log(1/alpha_0)) ** 0.5)  / int(self.count[arm])
            self.beta[arm] = self.main[arm] +self.remainder[arm]

            return self.sample_mean[arm] + self.beta[arm]

    def getReward(self, arm, reward):
        self.nbDraws[arm] += 1
        self.cumReward[arm] += reward
        self.t += 1
        
        self.rwd[arm, int(self.count[arm])] = reward
        self.count[arm] += 1
