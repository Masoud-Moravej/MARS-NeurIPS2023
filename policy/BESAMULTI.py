from math import sqrt, log
from statistics import mean
from random import choices,sample

from IndexPolicy import IndexPolicy

class BESAMULTI(IndexPolicy):

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
    
    def getReward(self, arm, reward):
        self.nbDraws[arm] += 1
        self.cumReward[arm] += reward
        self.t += 1
        self.RR[arm][self.nbDraws[arm]-1] = reward
    
    def computeIndex(self, arm):
        len_arm = len(arm)
        if len_arm > 2:
            arm_1 = self.computeIndex(arm[0:int(len_arm/2)])
            arm_2 = self.computeIndex(arm[int(len_arm/2):])
            if type(arm_1) is  list: arm_1 = arm_1[0]
            if type(arm_2) is  list: arm_2 = arm_2[0]
            arm = [arm_1,arm_2]
            len_arm = len(arm)
        if len_arm == 2:
            arm_ = arm[0]
            arm_other = arm[1]
            UCBALL_arm_other = 0
            UCBALL_arm_ = 0
            if self.nbDraws[arm_other] == 0: 
                UCBALL_arm_other = float('+infinity') 
            if self.nbDraws[arm_] == 0: 
                UCBALL_arm_ = float('+infinity') 
            
            if self.nbDraws[arm_other] != 0 and self.nbDraws[arm_] != 0:

                if self.nbDraws[arm_] > self.nbDraws[arm_other]:
                    II = sample(self.RR[arm_][0:self.nbDraws[arm_]], k=self.nbDraws[arm_other])
                else:
                    II = self.RR[arm_][0:self.nbDraws[arm_]]
                
                UCBALL_arm_ = mean(II)

                if self.nbDraws[arm_other] > self.nbDraws[arm_]:
                    II = sample(self.RR[arm_other][0:self.nbDraws[arm_other]], k=self.nbDraws[arm_])
                else:
                    II = self.RR[arm_other][0:self.nbDraws[arm_other]]
                
                UCBALL_arm_other = mean(II)
            if UCBALL_arm_other > UCBALL_arm_:
                return arm_other
            else:
                return arm_
            
        elif len_arm == 1:
            if type(arm) is list: 
                arm = arm[0]
            return arm
        else:
            print("smth wron!!!g")

        
    
    def choice(self):
        list_arms = list(range(self.nbArms))
        return self.computeIndex(list_arms)

