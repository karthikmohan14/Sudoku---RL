# Puzzle input index :
# ---------------------
# |  0 |  1 \  2 |  3 |
# |  4 |  5 \  6 |  7 |
# ---------------------
# |  8 |  9 \ 10 | 11 |
# | 12 | 13 \ 14 | 15 |
# ---------------------
import numpy as np 
import pickle
import json

ROWS = 4
COLS = 4

SIZE = ROWS * COLS

# 0 represents empty position

class State:
    def __init__(self):
        self.data = np.zeros((ROWS, COLS))
        pass

    # generate unique hash value
    def getHash(self):
        if self.hashVal is None:
            self.hashVal = 0
            for i in self.data.reshape(ROWS * COLS):
                if i == -1:
                    i = 2
                self.hashVal = self.hashVal * 3 + i
        return int(self.hashVal)
    
    # to determine puzzle solved or closed due to invalid state
    def isComplete(self):
        # base case / filled ?

        # row case

        # col case

        # box case

        pass

    # print puzzle
    def printSudoku(self):
        for i in range(0, ROWS):
            print('-------------')
            out = '| '
            for j in range(0, COLS):
                    token = self.data[i, j]
                out += token + ' | '
            print(out)
        print('-------------')        
        pass
    # end of class
    pass

def getAllStatesImpl(currentState, allStates):
    for i in range(0, ROWS):
        for j in range(0, COLS):
            pass
        pass
    pass

def getAllStates():

    return allStates

class bot:
    
    def __init__(self, step = 0.1, exploreRate=0.1):
        
        return
    def reset(self):
        return
    # accept a state
    def feedState(self,state):

        return
    # update estimation according to reward
    def feedReward(self, reward):

        return
    # possible actions:
    # {1,2,3,4,
    # 1,2,3,4,
    # 1,2,3,4
    # 1,2,3,4}
    def takeBlindAction(self):
        return action

    def savePolicy(self):
        fw = open('optimal_policy_' + str(self.), 'wb')
        pickle.dump(self.estimations, fw)
        fw.close()
        pass

    def loadPolicy(self):
        fr = open('optimal_policy_' + str(self.),'rb')
        self.estimations = pickle.load(fr)
        fr.close(
        pass    

    #  possible actions: list of remaining unfilled numbers    
    def takeAvailableAction(self):
        
        pass
    pass

def train():
    with open('td.json') as f:
    test_data = json.load(f)
    with open('tdsol.json') as f:
    test_data_sol = json.load(f)
    for i in range(20):
        sdk = test_data[i]
        sdk = np.reshape(sdk, (4, 4))
        sdkSol = test_data_sol[i]
        sdkSol = np.reshape(sdk, (4, 4))
    pass

def test():
    with open('trd.json') as f:
        train_data = json.load(f)
    with open('trdsol.json') as f:
        train_data_sol = json.load(f)
    for i in range(20):
        sdk = train_data[i]
        sdk = np.reshape(sdk, (4, 4))
        sdkSol = train_data_sol[i]
        sdkSol = np.reshape(sdk, (4, 4))
        pass
    pass

def run():

    pass    
train()
test()
run()   