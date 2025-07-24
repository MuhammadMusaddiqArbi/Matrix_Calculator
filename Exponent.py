import numpy as np
from Null_Matrix import Null_Matrix

def Exponent(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)

    exponent = np.exp(matrix)
    print(f"The exponent of the matrix is:\n{exponent}")
    return exponent