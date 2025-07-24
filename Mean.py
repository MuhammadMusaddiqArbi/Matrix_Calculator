import numpy as np
from Null_Matrix import Null_Matrix

def Mean(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    mean_value = matrix.mean()
    print(f"Mean value of the matrix:\n{matrix}\nis: {mean_value}")
    return mean_value