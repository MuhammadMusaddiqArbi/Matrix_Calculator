import numpy as np
from Null_Matrix import Null_Matrix

def Trigonometry(matrix):
    matrix = Null_Matrix(matrix)
    while True:
        print("1. Sin")
        print("2. Cos")
        print("3. Tan")
        print("4. ArcSin")
        print("5. ArcCos")
        print("6. ArcTan")
        print("7. Sinh")
        print("8. Cosh")
        print("9. Tanh")
        print("10. ArcSinh")
        print("11. ArcCosh")
        print("12. ArcTanh")
        print("13. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if choice > 13 or choice < 1:
            print("Enter a number between 1 and 13!")
            return
        elif choice == 13:
            print("Exiting your program......")
            return
        elif choice == 1:
            sin = np.sin(matrix)
            print(f"The sin of matrix is:\n{sin}")
            break
        elif choice == 2:
            cos = np.cos(matrix)
            print(f"The cos of the matrix is:\n{cos}")
            break
        elif choice == 3:
            tan = np.tan(matrix)
            print(f"The tan of the matrix is:\n{tan}")
            break
        elif choice == 4:
            if np.all((matrix >= -1) & (matrix <= 1)):
                arcsin = np.arcsin(matrix)
                print(f"The arcsin of the matrix is:\n{arcsin}")
            else:
                print("Error: All values for arcsin must be in [-1, 1].")
            break
        elif choice == 5:
            if np.all((matrix >= -1) & (matrix <= 1)):
                arccos = np.arccos(matrix)
                print(f"The arccos of the matrix is:\n{arccos}")
            else:
                print("Error: All values for arccos must be in [-1, 1].")
            break
        elif choice == 6:
            arctan = np.arctan(matrix)
            print(f"The arctan of the matrix is:\n{arctan}")
            break
        elif choice == 7:
            sinh = np.sinh(matrix)
            print(f"The sinh of the matrix is:\n{sinh}")
            break
        elif choice == 8:
            cosh = np.cosh(matrix)
            print(f"The cosh of the matrix is:\n{cosh}")
            break
        elif choice == 9:
            tanh = np.tanh(matrix)
            print(f"The tanh of the matrix is:\n{tanh}")
            break
        elif choice == 10:
            arcsinh = np.arcsinh(matrix)
            print(f"The arcsinh of the matrix is:\n{arcsinh}")
            break
        elif choice == 11:
            if np.all(matrix >= 1):
                arccosh = np.arccosh(matrix)
                print(f"The arccosh of the matrix is:\n{arccosh}")
            else:
                print("Error: All values for arccosh must be >= 1.")
            break
        elif choice == 12:
            if np.all((matrix > -1) & (matrix < 1)):
                arctanh = np.arctanh(matrix)
                print(f"The arctanh of the matrix is:\n{arctanh}")
            else:
                print("Error: All values for arctanh must be in (-1, 1).")
            break