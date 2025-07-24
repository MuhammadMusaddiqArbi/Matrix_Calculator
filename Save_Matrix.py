import numpy as np
from Null_Matrix import Null_Matrix

def Save_Matrix(matrix, file_path):
    matrix = Null_Matrix(matrix)
    try:
        np.savetxt(file_path, matrix, delimiter=',')
        print(f"Matrix saved to {file_path}:\n{matrix}")
    except Exception as e:
        print(f"Error saving matrix to {file_path}: {e}")