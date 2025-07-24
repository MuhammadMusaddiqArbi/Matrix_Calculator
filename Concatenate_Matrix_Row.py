import numpy as np
from Null_Matrix import Null_Matrix

def Concatenate_Matrix_Row(a, b):
    a = Null_Matrix(a)
    b = Null_Matrix(b)
    a = np.array(a)
    b = np.array(b)
    concatinated_Row = np.concatenate((a, b), axis=0)
    print(f"The concatenated matrix is\n:{concatinated_Row}")
    return concatinated_Row