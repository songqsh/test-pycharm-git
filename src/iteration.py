# print out all possible 3 by 3 sudoku
import itertools
cols = itertools.permutations(range(3))

tabs = itertools.permutations(cols,3)
counter = 0
for tab in tabs:
    print(tab)
    counter += 1

print(f'{counter} many tables')
