import numpy as np
from Null_Matrix import Null_Matrix

def Ravel(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)

    ravelled = np.ravel(matrix)
    print(f"The ravelled matrix is:\n{ravelled}")
    return ravelled