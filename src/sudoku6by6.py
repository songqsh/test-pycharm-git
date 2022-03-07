# we want to solve sudoku 6 by 6

import numpy as np
from itertools import permutations

tab = np.zeros((3, 3), dtype=int)
perm = permutations([1,2,3])
for i in perm:
    #print(tab[])
    print(f"{i}, {type(i)}")
for i in range(3):
    print(f"{tab[i]}")

