import numpy as np
from Null_Matrix import Null_Matrix

def Log_Functions(matrix):
    matrix = Null_Matrix(matrix)
    matrix = np.array(matrix)

    while True:
        print("1. Log Base 1 of the matrix")
        print("2. Log Base 2 of the matrix")
        print("3. Log Base 10 of the matrix")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            log = np.log(matrix)
            print(f"Log Base 1 of the matrix is: \n{log}")
            return log
        elif choice == 2:
            log2 = np.log2(matrix)
            print(f"Log Base 2 of the matrix is: \n{log2}")
            return log2
        elif choice == 3:
            log10 = np.log10(matrix)
            print(f"Log Base 10 of the matrix is: \n{log10}")
            return log10
        else:
            print("Invalid choice. Please choose a valid option.")


