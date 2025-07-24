import numpy as np
from Null_Matrix import Null_Matrix

def Addition(a, b):
    a = Null_Matrix(a)
    b = Null_Matrix(b)
    if len(a) == len(b):
        if np.shape(a) == np.shape(b):
            a = np.array(a)
            b = np.array(b)
            print(f"Adding matrices:\n{a}\n+\n{b}")
            add = a + b
            print(f"Resulting matrix:\n{add}")
            return add
        else:
            raise ValueError("Matrices must have the same dimensions for addition.")
    else:
        raise ValueError("Matrices must have the same dimensions for addition.")
    
