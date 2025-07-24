import numpy as np
from Null_Matrix import Null_Matrix

def Append_To_Row(matrix, new_row):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    new_row = np.array(new_row)
    matrix = np.append(matrix, [new_row], axis=0)
    print(f"Matrix after appending new row:\n{matrix}")
    return matrix

