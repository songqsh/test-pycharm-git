# solve sudoku 4 by 4 using qp-solver
import numpy as np
from qpsolvers import solve_qp

# sudoku setup
sudoku_dim = 4
box_row_n = box_col_n = 2

# sudoku table initialization with 3d-tensor
# each entry of the table takes a value in between 0 and 1
tab = np.zeros((sudoku_dim, sudoku_dim, sudoku_dim))


# convert 3d to 1d
def conversion_3d_1d(row_i, col_i, num_i):
    return sudoku_dim ** 2 * row_i + sudoku_dim * col_i + num_i

# coefficient matrix A for Ax = b
mat_A_dim = sudoku_dim ** 3

# construct matrix A as a list
mat_A = []
vec_b = []

for i in range(sudoku_dim):
    for j in range(sudoku_dim):
        row = [0] * mat_A_dim  # initialize a row
        for k in range(sudoku_dim):
            row[sudoku_dim ** 2 * i + sudoku_dim * j + k] = 1.  # coefficient from the constraint
        mat_A += [row]
        vec_b += [1.]

for i in range(sudoku_dim):
    for k in range(sudoku_dim):
        row = [0] * mat_A_dim  # initialize a row
        for j in range(sudoku_dim):
            row[sudoku_dim ** 2 * i + sudoku_dim * j + k] = 1.  # coefficient from the constraint
        mat_A += [row]
        vec_b += [1.]

for j in range(sudoku_dim):
    for k in range(sudoku_dim):
        row = [0] * mat_A_dim  # initialize a row
        for i in range(sudoku_dim):
            row[sudoku_dim ** 2 * i + sudoku_dim * j + k] = 1.  # coefficient from the constraint
        mat_A += [row]
        vec_b += [1.]

# box constraints
for ll in range(2):
    for m in range(2):
        for k in range(4):
            row = [0] * mat_A_dim  # initialize a row
            for lp in range(2):
                for mp in range(2):
                    ind = sudoku_dim ** 2 * (2 * ll + lp) + sudoku_dim * (2 * m + mp) + k
                    row[ind] = 1.
            mat_A += [row]
            vec_b += [1.]

# a list with given members [row_index, col_index, value]
given_nums = [[0, 0, 1],
              [0, 1, 2],
              [3, 2, 2],
              [3, 3, 4]]
# Set up matrix P and q in the objective function
mat_P = np.zeros((mat_A_dim, mat_A_dim))
vec_q = np.zeros((mat_A_dim, 1))
for a_given_num in given_nums:
    ind = int(sudoku_dim ** 2 * a_given_num[0] + sudoku_dim * a_given_num[1] + (a_given_num[2]-1))
    mat_P[ind, ind] = 1.
    vec_q[ind, 0] = -2.

# bounds
lb = np.zeros((mat_A_dim, 1))
ub = lb + 1

x = solve_qp(P=mat_P, q=vec_q, A = np.array(mat_A), b = np.array(vec_b), lb=lb, ub=ub)
print(f"QP solution: x = {x}")


