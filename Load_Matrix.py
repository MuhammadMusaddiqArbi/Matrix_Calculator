import numpy as np

def Load_Matrix(file_path):
    try:
        matrix = np.loadtxt(file_path, delimiter=',')
        print(f"Matrix loaded from {file_path}:\n{matrix}")
        return matrix
    except Exception as e:
        raise Exception(f"Error loading matrix from {file_path}: {str(e)}")
    except ValueError as ve:
        raise Exception(f"[Matrix Load Error] Invalid value in file '{file_path}'. Make sure the matrix contains only numbers.\nOriginal Error: {ve}")
    except FileNotFoundError:
        raise Exception(f"[Matrix Load Error] File '{file_path}' not found.")
