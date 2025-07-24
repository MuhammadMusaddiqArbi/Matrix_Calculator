import numpy as np
from Null_Matrix import Null_Matrix

def Maximum(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    maximum = matrix.max()
    print(f"Maximum value in the matrix:\n{matrix}\nis: {maximum}")
    return maximum