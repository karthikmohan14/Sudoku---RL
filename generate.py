import timeit
import numpy as np
import random as rd

start_time = timeit.default_timer()
# code you want to evaluate

class Sudoku:
    def __init__(self):
        self.size = 9
        self.cell = np.arange(1,self.size+1)
        rd.shuffle(self.cell)
        self.cells = np.array([self.cell])
        for x in range(9):
            rd.shuffle(self.cell)
            self.cells = np.vstack([self.cells,self.cell])
            pass
        print(self.cells)
        pass
    # sudoku sorted in self.cells
    def printSudoku(self):
        i=0
        while( i <= 6 ):
            j=0
            while( j <= 6 ):
                # print(self.cells[i][j]," ",self.cells[i][j+1])
                print(self.cells[i][j]," ",self.cells[i][j+1]," ",self.cells[i][j+2]," | ",self.cells[i+1][j]," ",self.cells[i+1][j+1]," ",self.cells[i+1][j+2]," | ",self.cells[i+2][j]," ",self.cells[i+2][j+1]," ",self.cells[i+2][j+2])
                j+=3
                pass
            print("-------------------------------------")
            i+=3
            pass
        pass
lassie = Sudoku();
lassie.printSudoku()
elapsed = timeit.default_timer() - start_time
print(elapsed)