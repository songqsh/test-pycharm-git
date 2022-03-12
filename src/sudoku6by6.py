# we want to solve sudoku 6 by 6

# import numpy as np
from itertools import permutations
row_num = 5
rows = permutations(range(row_num))
tabs = permutations(rows, row_num)
counter = 0
for tab in tabs:
    # print(np.array(tab))
    # print('=============')
    counter += 1
print(f"There are \n {counter} many tables")
