import numpy as np
from Null_Matrix import Null_Matrix

def Delete_Column(matrix, column):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    if column < 0 or column >= matrix.shape[1]:
        raise IndexError("Column index out of bounds.")
    matrix = np.delete(matrix, column, axis=1)
    print(f"Matrix after deleting column {column}:\n{matrix}")
    return matrix