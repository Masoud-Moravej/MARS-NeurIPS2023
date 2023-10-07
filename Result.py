import numpy as np

class Result:
    def __init__(self, nbArms, horizon):
        self.nbArms = nbArms
        self.choices = np.zeros(horizon)
        self.rewards = np.zeros(horizon)
    
    def store(self, t, choice, reward):
        self.choices[t] = choice
        self.rewards[t] = reward
    
    def getNbPulls(self):
        if (self.nbArms==float('inf')):
            self.nbPulls=np.array([])
            pass
        else :
            nbPulls = np.zeros(self.nbArms)
            for choice in self.choices:
                nbPulls[int(choice)] += 1
            return nbPulls
    
    def getRegret(self, bestExpectation):
        return np.cumsum(bestExpectation-self.rewards)
