import numpy as np
import random as rd

size = 9
cell = np.arange(1,size+1)
rd.shuffle(cell)
cells = np.array([cell])
for x in range(9):
    rd.shuffle(cell)
    cells = np.vstack([cells,cell])
    pass
print(cells)
i=0
while( i <= 6 ):
    j=0
    while( j <= 6 ): 
        # print(cells[i][j]," ",cells[i][j+1])
        print(cells[i][j]," ",cells[i][j+1]," ",cells[i][j+2]," | ",cells[i+1][j]," ",cells[i+1][j+1]," ",cells[i+1][j+2]," | ",cells[i+2][j]," ",cells[i+2][j+1]," ",cells[i+2][j+2])
        j+=3
        pass
    print("-------------------------------------")    
    i+=3
    pass        
