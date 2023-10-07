from Result import *
from Environment import Environment

class MAB(Environment):

    def __init__(self, arms):
        self.arms = arms
        self.nbArms = len(arms)

    def play(self, policy, horizon):
        policy.startGame()
        result = Result(self.nbArms, horizon)
        for t in range(horizon):
            choice = policy.choice()
            reward = self.arms[choice].draw()
            policy.getReward(choice, reward)
            result.store(t, choice, reward)
        return result
