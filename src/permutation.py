# given a list, we want to identify it is a permutation
# this will use set
import numpy as np


def is_permutation(test_list, n):
    pool = set(range(1, n + 1))
    return (len(pool) == len(test_list)) and (pool == set(test_list))


list1 = np.array([1, 3, 2])
print(is_permutation(list1, 3))
