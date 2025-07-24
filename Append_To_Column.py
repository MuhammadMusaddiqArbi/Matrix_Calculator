import numpy as np
from Null_Matrix import Null_Matrix

def Append_To_Column(matrix, new_column):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    matrix = np.append(matrix, [new_column], axis=1)
    print(f"Matrix after appending new column:\n{matrix}")
    return matrix