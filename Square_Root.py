import numpy as np
from Null_Matrix import Null_Matrix

def Square_Root(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    squareroot = np.sqrt(matrix)
    print(f"The square of matrix is:\n{squareroot}")
    return squareroot