import numpy as np
from Null_Matrix import Null_Matrix

def Determinant(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix is not square")
    print(f"Calculating determinant of the matrix:\n{matrix}")
    det = np.linalg.det(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and does not have a determinant.")
    print(f"Determinant is: {det}")
    return det
