import numpy as np
from Null_Matrix import Null_Matrix

def Inverse(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    try:
        inv_matrix = np.linalg.inv(matrix)
        print(f"Inverse of the matrix:\n{matrix}\nis:\n{inv_matrix}")
        return inv_matrix
    except np.linalg.LinAlgError:
        raise ValueError("Matrix is singular and cannot be inverted.")