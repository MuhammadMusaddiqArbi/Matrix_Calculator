import numpy as np
from Null_Matrix import Null_Matrix

def Flatten(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)

    flattened = matrix.flatten()
    print(f"The flattened array is:\n{flattened}")
    return flattened