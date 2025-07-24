import numpy as np
from Null_Matrix import Null_Matrix

def Stack_Matrix_Row(a, b):
    a = Null_Matrix(a)
    b = Null_Matrix(b)

    a = np.array(a)
    b = np.array(b)
    stacked_row = np.vstack((a, b))
    print(f"Matrix after stacked by row:\n{stacked_row}")
    return stacked_row