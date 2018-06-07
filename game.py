# import dependencies
from __future__ import print_function
import numpy as np
import json
import random
import math


class environ:

    # init with random sudoku
    def __init__(self):
        with open('trd.json') as f:
            self.train_data = json.load(f)
        self.key = random.randint(0, len(self.train_data)-1)
        self.sudoku = self.train_data[self.key]
        # print(key)
        self.action_space = len(self.sudoku)
        self.observation_space = math.pow(
            self.action_space, (self.action_space/2))

    def render(self):
        print(self.sudoku)
        pass

    def reset(self):
        self.key = random.randint(0, len(self.train_data)-1)
        self.sudoku = self.train_data[self.key]
        self.action_space = len(self.sudoku)
        self.observation_space = math.pow(
            self.action_space, (self.action_space/2))
        pass

    def spot_select(self):
        indices = [index for index in range(
            len(self.sudoku)) if self.sudoku[index] == 0]
        r = random.randint(0, len(indices)-1)
        return indices[r]

    def step(self):
        # base case : no steps to be taken if all 0s are filled , maximum reward
        if self.sudoku.count(0) == 0:
            reward = 10
            truth = True
            state_prime = self.sudoku
            pass
        else:
            spot = self.spot_select()
            # pick an empty spot and fill with any of the numbers from 1,2,3,4
            num = random.randint(1, 4)
            state_prime = self.sudoku
            state_prime[spot] = num
            if state_prime[spot] == self.train_data_sol[self.key][spot]:
                # positive reward
                reward = 1
                pass
            else:
                # negative reward
                reward = -1
                truth = False
                pass
        return state_prime, reward, truth
    # end of class definition
    pass


# load env
env = environ()
env.render()
print()

print("number of actions : ", env.action_space)
print("number of states : ", env.observation_space)


def epsilon_greedy(Q, s, na):
    epsilon = 0.3
    p = np.random.uniform(low=0, high=1)
    # print(p)
    if p > epsilon:
        return np.argmax(Q[s, :])
    else:
        return env.action_space.sample()


# q learning implementation
Q = np.zeros([env.observation_space, env.action_space])

# set hyper parameters
lr = 0.5
y = 0.9
eps = 10000

for i in range(eps):
    s = env.reset()
    t = False
    while(True):
        a = epsilon_greedy(Q, s, env.action_space.n)
        s_, r, t = env.step(a)
        if(r == 0):
            if t == True:
                r = -5
                Q[s_] = np.ones(env.action_space.n)*r
                pass
            else:
                r = -1
                pass
            pass
        if(r == 1):
            r = 100
            Q[s_] = np.ones(env.action_space.n)*r
            pass
        Q[s, a] = Q[s, a] + lr * (r + y*np.max(Q[s_, a]) - Q[s, a])
        s = s_
        if(t == True):
            break
    pass


print("Q table : ")
print(Q)
print()

print("Output after learning : ")
print()

s = env.reset()
env.render()

while(True):
    a = np.argmax(Q[s])
    s_, r, t = env.step(a)
    print("===============")
    env.render()
    s = s_
    if(t == True):
        break
