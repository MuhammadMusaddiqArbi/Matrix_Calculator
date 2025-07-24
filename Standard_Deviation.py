import numpy as np
from Null_Matrix import Null_Matrix

def Standard_Deviation(matrix):
    matrix = Null_Matrix(matrix)
    
    matrix = np.array(matrix)
    std_dev = np.std(matrix)
    print(f"Standard Deviation of the matrix:\n{matrix}\nis: {std_dev}")
    return std_dev