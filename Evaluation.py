import numpy as np

class Evaluation:
  
    def __init__(self, env, pol, nbRepetitions, horizon, tsav=[]):
        if len(tsav)>0:
            self.tsav = tsav
        else:
            self.tsav = np.arange(horizon)
        self.env = env
        self.pol = pol
        self.nbRepetitions = nbRepetitions
        self.horizon = horizon
        self.nbArms = env.nbArms
        self.nbPulls = np.zeros((self.nbRepetitions, self.nbArms))
        self.cumReward = np.zeros((self.nbRepetitions, len(tsav)))

        for k in range(nbRepetitions): 
            if nbRepetitions < 10 or k % (nbRepetitions/10)==0:
                print(k)
            result = env.play(pol, horizon)
            self.nbPulls[k,:] = result.getNbPulls()
            self.cumReward[k,:] = np.cumsum(result.rewards)[tsav]
     
    def meanReward(self):
        return sum(self.cumReward[:,-1])/len(self.cumReward[:,-1])



    def meanNbDraws(self):
        return np.mean(self.nbPulls ,0) 

    def meanRegret(self):
        return (1+self.tsav)*max([arm.expectation for arm in self.env.arms]) - np.mean(self.cumReward, 0)
    
    def varReward(self):
        return np.var(self.cumReward, 0)
    
    def varRegret(self):
        regret_ = (1+self.tsav)*max([arm.expectation for arm in self.env.arms]) - self.cumReward
        return np.var(regret_, 0)
