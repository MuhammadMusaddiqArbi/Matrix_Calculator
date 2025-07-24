import numpy as np
from Null_Matrix import Null_Matrix

def Split_Columns(matrix, column):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)

    splitted_column = np.split(matrix, [column], axis=1)
    print(f"The splitted matrix is:\n{splitted_column}")
    return splitted_column