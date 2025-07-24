import numpy as np
from Null_Matrix import Null_Matrix

def Scalar_Multiplication(scalar, matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    print(f"Multiplying matrix by scalar {scalar}:\n{matrix}")
    result = scalar * matrix
    print(f"Resulting matrix:\n{result}")
    return result
