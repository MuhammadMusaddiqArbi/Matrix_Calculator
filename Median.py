import numpy as np
from Null_Matrix import Null_Matrix

def Median(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    median_value = np.median(matrix)
    print(f"Median value of the matrix:\n{matrix}\nis: {median_value}")
    return median_value