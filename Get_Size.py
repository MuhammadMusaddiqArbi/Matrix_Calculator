import numpy as np
from Null_Matrix import Null_Matrix

def Get_Size(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)

    size = np.size(matrix)
    print(f"The size of the matrix is: {size}")
    return size