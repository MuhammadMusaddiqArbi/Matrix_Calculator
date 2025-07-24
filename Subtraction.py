import numpy as np
from Null_Matrix import Null_Matrix

def Subtraction(a, b):
    a = Null_Matrix(a)
    b = Null_Matrix(b)
    if len(a) == len(b):
        if np.shape(a) == np.shape(b):
            a = np.array(a)
            b = np.array(b)
            print(f"Subtracting matrices:\n{a}\n-\n{b}")
            sub = a - b
            print(f"Resulting matrix:\n{sub}")
            return sub
        else:
            raise ValueError("Matrices must have the same dimensions")
    else:
        raise ValueError("Matrices must have the same dimensions for subtraction.")