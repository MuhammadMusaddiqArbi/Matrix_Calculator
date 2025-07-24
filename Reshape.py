import numpy as np
from Null_Matrix import Null_Matrix

def Reshape(matrix, x, y):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)

    reshaped = np.reshape(matrix, (x, y))
    print(f"The reshaped matrix is:\n{reshaped}")
    return reshaped