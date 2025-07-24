import numpy as np
from Null_Matrix import Null_Matrix

def Rank(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)
    rank_value = np.linalg.matrix_rank(matrix)
    print(f"Rank of the matrix:\n{matrix}\nis: {rank_value}")
    return rank_value