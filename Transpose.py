import numpy as np
from Null_Matrix import Null_Matrix

def Transpose(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    print(f"Transposing the matrix:\n{matrix}")
    print(f"Transposed matrix:\n{matrix.T}")
    return matrix.T