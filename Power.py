import numpy as np
from Null_Matrix import Null_Matrix

def Power(matrix, exponent):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    
    power = np.power(matrix, exponent)
    print(f"The matrix to the power {exponent} is:\n{power}")
    return power