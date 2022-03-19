# solve sudoku 4 by 4 using qp-solver

import numpy as np
import qpsolvers as qp

# sudoku setup
sudoku_dim = 4
box_row_n = box_col_n = 2


# convert 3d to 1d
def conversion_3d_1d(row_i, col_i, num_i):
    return int(sudoku_dim ** 2 * row_i + sudoku_dim * col_i + num_i)


# coefficient matrix A and b for Ax = b
n_decision_variables = sudoku_dim ** 3


# produce a row of A by checking squares
def square_condition(row_i, col_i):
    row = [0] * n_decision_variables  # initialize a row
    for num_i in range(sudoku_dim):
        ind = conversion_3d_1d(row_i, col_i, num_i)
        row[ind] = 1.  # coefficient from the constraint
    return row


# produce a row of A by checking columns
def column_condition(row_i, num_i):
    row = [0] * n_decision_variables  # initialize a row
    for col_i in range(sudoku_dim):
        ind = conversion_3d_1d(row_i, col_i, num_i)
        row[ind] = 1.  # coefficient from the constraint
    return row


# produce a row of A by checking rows
def row_condition(col_i, num_i):
    row = [0] * n_decision_variables  # initialize a row
    for row_i in range(sudoku_dim):
        ind = conversion_3d_1d(row_i, col_i, num_i)
        row[ind] = 1.  # coefficient from the constraint
    return row


# produce a row of A by checking small boxes
def box_condition(box_i):
    row = [0] * n_decision_variables  # initialize a row
    indices = []
    for row_i in range(2):
        for col_i in range(2):
            indices += [[2 * box_i[0] + row_i, 2 * box_i[1] + col_i]]
    for row_col_i in indices:
        for num_i in range(4):
            ind = conversion_3d_1d(row_col_i[0], row_col_i[1], num_i)
            row[ind] = 1.  # coefficient from the constraint
    return row


# construct matrix A as a list
mat_A = []

for i in range(sudoku_dim):
    for j in range(sudoku_dim):
        mat_A += [square_condition(i, j)]
        mat_A += [column_condition(i, j)]
        mat_A += [row_condition(i, j)]

vec_b = [1]*len(mat_A)

# a list with given members [row_index, col_index, value]
given_nums = [[0, 0, 1],
              [0, 1, 2],
              [3, 2, 2],
              [3, 3, 4]]
# Set up matrix P and q in the objective function
# mat_P = np.zeros((n_decision_variables, n_decision_variables))
mat_P = .01*np.eye(n_decision_variables)
vec_q = np.zeros(n_decision_variables)
for a_given_num in given_nums:
    ind = conversion_3d_1d(a_given_num[0], a_given_num[1], a_given_num[2]-1)
    mat_P[ind, ind] += 1.
    vec_q[ind] = -2.

# bounds
lb = np.zeros(n_decision_variables)
ub = lb + 1

mat_A = np.array(mat_A)
vec_b = np.array(vec_b)

print(qp.available_solvers)
x = qp.solve_qp(P=mat_P, q=vec_q, A = mat_A, b = vec_b, lb=lb, ub=ub, solver='quadprog')
#x = qp._solve_qp(P=mat_P, q=vec_q, A = mat_A, b = vec_b, lb=lb, ub=ub)
#print(f"QP solution: x = {x}")
