# print out all possible sudoku
import itertools
import numpy as np

row_num = 2

rows = itertools.permutations(range(row_num))
tabs = itertools.permutations(rows, row_num)
counter = 0
for tab in tabs:
    print(np.array(tab))
    print('=============')
    counter += 1

print(f'{counter} many tables')
