import numpy as np
from Null_Matrix import Null_Matrix

def Split_Rows(matrix, row):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)

    splittedrow = np.split(matrix, [row], axis=0)
    print(f"The matrix splitted by rows is:\n{splittedrow}")
    return splittedrow