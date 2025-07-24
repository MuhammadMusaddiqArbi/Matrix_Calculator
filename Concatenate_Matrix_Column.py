import numpy as np
from Null_Matrix import Null_Matrix

def Concatenate_Matrix_Column(a, b):
    a = Null_Matrix(a)
    b = Null_Matrix(b)
    a = np.array(a)
    b = np.array(b)
    concatenated_column = np.concatenate((a,b), axis=1)
    print(f"The concatenated matrix is:\n{concatenated_column}")
    return concatenated_column