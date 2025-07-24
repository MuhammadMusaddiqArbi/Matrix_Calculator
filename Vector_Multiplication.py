import numpy as np
from Null_Matrix import Null_Matrix

def Vector_Multiplication(a, b):
    a = Null_Matrix(a)
    b = Null_Matrix(b)
    if len(a) == len(b):
        a = np.array(a)
        b = np.array(b)
        print(f"Multiplying vectors:\n{a}\n*\n{b}")
        result = a * b
        print(f"Resulting vector:\n{result}")
        return result
    else:
        raise ValueError("Vectors must have the same dimensions for multiplication.")