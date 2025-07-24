import numpy as np
from Null_Matrix import Null_Matrix

def Delete_Row(matrix, row):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    if row < 0 or row >= matrix.shape[0]:
        raise IndexError("Row index out of bounds.")
    matrix = np.delete(matrix, row, axis=0)
    print(f"Matrix after deleting row {row}:\n{matrix}")
    return matrix