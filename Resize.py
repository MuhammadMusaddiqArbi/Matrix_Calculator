import numpy as np
from Null_Matrix import Null_Matrix

def Resize(matrix, x, y):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)

    resized = np.resize(matrix, (x, y))
    print(f"The resized matrix is:\n{resized}")
    return resized