import numpy as np

def Null_Matrix(matrix):
    if matrix is None:
        raise ValueError("Create or Load a matrix")
    else:
        return matrix