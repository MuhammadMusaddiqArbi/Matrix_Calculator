import numpy as np
from Null_Matrix import Null_Matrix

def Dot_Multiplication(a, b):
    a = Null_Matrix(a)
    b = Null_Matrix(b)
    if len(a[0]) == len(b):
        a = np.array(a)
        b = np.array(b)
        print(f"Dot multiplying matrices:\n{a}\n.\n{b}")
        result = np.dot(a, b)
        print(f"Resulting matrix:\n{result}")
        return result
    else:
        raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix for dot multiplication.")