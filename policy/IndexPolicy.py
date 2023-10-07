from random import choice

from Policy import *

class IndexPolicy(Policy):

    def choice(self):
        index = dict()
        for arm in range(self.nbArms):
            index[arm] = self.computeIndex(arm)
        maxIndex = max (index.values())
        bestArms = [arm for arm in index.keys() if index[arm] == maxIndex]
        return choice(bestArms)
