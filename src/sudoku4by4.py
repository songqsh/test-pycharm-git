# we want to solve sudoku 4 by 4
from itertools import permutations

import numpy as np

# sudoku setup
sudoku_dim = 4
box_row_n = box_col_n = 2
# a list with given members [row_i, col_i, val]
given_nums = [[0, 0, 1],
              [0, 1, 2],
              [3, 2, 2],
              [3, 3, 4]]


# check if a given list is a permutation of {1,2, ..., n}
def is_permutation(test_list, number):
    pool = set(range(1, number + 1))
    return (len(pool) == len(test_list)) and (pool == set(test_list))


# all candidate sudoku in a permutation
rows = permutations(range(1, sudoku_dim + 1))
tabs = permutations(rows, sudoku_dim)

counter = 0
for tab in tabs:
    nptab = np.array(tab)
    feasibility = 1
    # check each column
    for col_i in range(sudoku_dim):
        test = is_permutation(nptab[:, col_i], sudoku_dim)
        if test is False:
            feasibility = 0
            break
    # check each box
    for box_row_i in range(2):
        for box_col_i in range(2):
            if feasibility == 0:
                break
            box_entries = list(nptab[2*box_row_i, 2*box_col_i:2*box_col_i+2])
            box_entries += list(nptab[2*box_row_i+1, 2*box_col_i:2*box_col_i+2])
            test = is_permutation(box_entries, sudoku_dim)
            if test is False:
                feasibility = 0
                break
    # check given numbers in the table
    for i in given_nums:
        if feasibility == 0:
            break
        if nptab[i[0], i[1]] != i[2]:
            feasibility = 0
            break

    if feasibility == 1:
        print(nptab)
        print(f'==================')
        counter += 1
print(f"There are {counter} many tables")
