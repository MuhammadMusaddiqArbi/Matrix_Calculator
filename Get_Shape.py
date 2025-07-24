import numpy as np
from Null_Matrix import Null_Matrix

def Get_Shape(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)

    shape = np.shape(matrix)
    print(f"The shape of the matrix is: {shape}")
    return shape