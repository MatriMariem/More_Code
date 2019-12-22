#!/usr/bin/python3
def detmatrix(matrix):
    if len(matrix) != len(matrix[0]):
        print("non_square matrix have no determinant")
        return None
    if len(matrix) == len(matrix[0]) and len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    mat = matrix[:]
    sign = 1
    for j in range(len(mat[0])):
        mat[0][j] *= sign
        sign *= -1
    det = 0
    for j in range(len(mat[0])):
        small_matrix = mat[1:]
        for i in range(len(small_matrix)):
            small_matrix[i] = small_matrix[i][0:j] + small_matrix[i][j+1:]
        det += mat[0][j] * detmatrix(small_matrix)
    return det

print(detmatrix([[1, 3, 5, 9], [1, 3, 1, 7], [4, 3, 9, 7], [5, 2, 0, 9]]))
