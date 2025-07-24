import numpy as np
from Null_Matrix import Null_Matrix

def Minimum(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    minimum = matrix.min()
    print(f"Minimum value in the matrix:\n{matrix}\nis: {minimum}")
    return minimum