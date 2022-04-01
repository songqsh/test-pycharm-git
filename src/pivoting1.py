# import packages
import numpy as np

np.set_printoptions(suppress=True)


# pivoting with (i,j)
def pivoting(A_mat, row_i, col_i):
    if A_mat[row_i, col_i] == 0:
        print(f'err msg: no pivoting due to division by zero')
        return 0
    A_mat[row_i] = A_mat[row_i] / A_mat[row_i, col_i]  # scale to get one in (row_i,col_i)
    n_rows, _ = A_mat.shape
    for k in range(n_rows):
        if k == row_i:
            continue  # skip i-row
        A_mat[k] = A_mat[k] - A_mat[row_i] * A_mat[k, col_i]  # replacement to get zero


# matrix input
M = np.array([[1, 2, -1, 4.], [-1., -1, 2, 1], [0., 1, 1, 6]])
print(f'{M}')


pivoting(M, 0, 0)
print(f'----\n {M}')

pivoting(M, 1, 1)
print(f'----\n {M}')

pivoting(M, 2, 2)
print(f'----\n {M}')
