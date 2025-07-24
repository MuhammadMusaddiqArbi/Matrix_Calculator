import numpy as np

from Create_Matrix import Create_Matrix
from Load_Matrix import Load_Matrix
from Save_Matrix import Save_Matrix
from Get_Size import Get_Size
from Get_Shape import Get_Shape
from Resize import Resize
from Reshape import Reshape
from Flatten import Flatten
from Ravel import Ravel
from Addition import Addition
from Subtraction import Subtraction
from Square_Root import Square_Root
from Exponent import Exponent
from Power import Power
from Logarithmic_Functions import Log_Functions
from Dot_Multiplication import Dot_Multiplication
from Vector_Multiplication import Vector_Multiplication
from Scalar_Multiplication import Scalar_Multiplication
from Trigonometry import Trigonometry  
from Transpose import Transpose
from Determinant import Determinant
from Inverse import Inverse
from Rank import Rank
from Minimum import Minimum
from Maximum import Maximum
from Mean import Mean
from Median import Median
from Standard_Deviation import Standard_Deviation
from Append_To_Row import Append_To_Row
from Append_To_Column import Append_To_Column
from Delete_Row import Delete_Row
from Delete_Column import Delete_Column
from Concatenate_Matrix_Row import Concatenate_Matrix_Row
from Concatenate_Matrix_Column import Concatenate_Matrix_Column
from Stack__Matrix_Row import Stack_Matrix_Row
from Stack_Matrix_Column import Stack_Matrix_Column
from Split_Rows import Split_Rows
from Split_Columns import Split_Columns
from Null_Matrix import Null_Matrix

def main():
    current_matrix = None
    current_matrix_2 = None
    while True:
        input("Enter Enter to continue! ")
        print("------------------------------------------------------------------------")
        print("\nMatrix Calculator Menu")
        print("1. Create Matrix")
        print("2. Load Matrix")
        print("3. Save Matrix")
        print("4. Get Size Of Matrix")
        print("5. Get Shape Of Matrix")
        print("6. Resize Matrix")
        print("7. Rehape Matrix")
        print("8. Flatten Matrix")
        print("9. Ravel Matrix")
        print("10. Add Matrices")
        print("11. Subtract Matrices")
        print("12. Square Root of Matrix")
        print("13. Exponent of Matrix")
        print("14. Power Of Matrix")
        print("15. Logarithmic Functions of Matrix")
        print("16. Dot Multiplication of Matrices")
        print("17. Vector Multiplication of Matrices")
        print("18. Scalar Multiplication of Matrices")
        print("19. Trigonometry of Matrices")
        print("20. Transpose of Matrix")
        print("21. Determinant of Matrix")
        print("22. Inverse of Matrix")
        print("23. Rank of Matrix")
        print("24. Minimum of Matrix")
        print("25. Maximum of Matrix")
        print("26. Mean of Matrix")
        print("27. Median of Matrix")
        print("28. Standard Deviation of Matrix")
        print("29. Append Row to Matrix")
        print("30. Append Column to Matrix")
        print("31. Delete Row from Matrix")
        print("32. Delete Column from Matrix")
        print("33. Concatenate Matrix Row")
        print("34. Concatenate Matrix Column")
        print("35. Stack Matrix Row")
        print("36. Stack Matrix Column")
        print("37. Split Rows of Matrix")
        print("38. Split Columns of Matrix")
        print("39. Check if matrix is NULL")
        print("40. Exit")
        print("------------------------------------------------------------------------")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice > 40 or choice < 1:
            print("Enter a number between 1 and 39")
            continue

        elif choice == 40:
            print("Exiting the program......")
            break

        elif choice == 1:
            rows = int(input("Enter Number Of Rows: "))
            columns = int(input("Enter Number Of Columns: "))
            current_matrix = Create_Matrix(rows, columns)

        elif choice == 2:
            file_path = input("Enter file path: ")
            current_matrix = Load_Matrix(file_path)
            continue

        elif choice == 3:
            file_path = input("Enter file path: ")
            Save_Matrix(current_matrix, file_path)
            continue

        elif choice == 4:
            size = Get_Size(current_matrix)
            continue

        elif choice == 5:
            shape = Get_Shape(current_matrix)
            continue

        elif choice == 6:
            row = int(input("Enter Row Index: "))
            column = int(input("Enter Column Index: "))
            resize = Resize(current_matrix, row, column)
            continue

        elif choice == 7:
            row = int(input("Enter Row Index: "))
            column = int(input("Enter Column Index: "))
            reshape = Reshape(current_matrix, row, column)
            continue

        elif choice == 8:
            flatten = Flatten(current_matrix)
            continue

        elif choice == 9:
            ravel = Ravel(current_matrix)
            continue

        elif choice == 10:
            print("How do you want to input Matrix A")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_a = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_a = Load_Matrix(file_path)

            print("How do you want to input Matrix B")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_b = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_b = Load_Matrix(file_path)    
            add = Addition(matrix_a, matrix_b)
            continue

        elif choice == 11:
            print("How do you want to input Matrix A")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_a = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_a = Load_Matrix(file_path)

            print("How do you want to input Matrix B")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_b = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_b = Load_Matrix(file_path)    
            sub = Subtraction(matrix_a, matrix_b)
            continue

        elif choice == 12:
            squareroot = Square_Root(current_matrix)
            continue

        elif choice == 13:
            exponent = Exponent(current_matrix)
            continue

        elif choice == 14:
            exponent = int(input("Enter exponent:"))
            power = Power(current_matrix, exponent)
            continue
        
        elif choice == 15:
            logarithmic = Log_Functions(current_matrix)
            continue

        elif choice == 16:
            print("How do you want to input Matrix A")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_a = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_a = Load_Matrix(file_path)

            print("How do you want to input Matrix B")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_b = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_b = Load_Matrix(file_path)    

            dot_multiply = Dot_Multiplication(matrix_a, matrix_b)
            continue

        elif choice == 17:
            print("How do you want to input Matrix A")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_a = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_a = Load_Matrix(file_path)

            print("How do you want to input Matrix B")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_b = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_b = Load_Matrix(file_path)   

            vector_multiply = Vector_Multiplication(matrix_a, matrix_b)
            continue

        elif choice == 18:
            print("How do you want to input Matrix A")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_a = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_a = Load_Matrix(file_path)

            print("How do you want to input Matrix B")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_b = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_b = Load_Matrix(file_path)    

            scalar_multiply = Scalar_Multiplication(matrix_a, matrix_b)
            continue

        elif choice == 19:
            trigonometry = Trigonometry(current_matrix)
            continue

        elif choice == 20:
            transpose = Transpose(current_matrix)
            continue

        elif choice == 21:
            determinant = Determinant(current_matrix)
            continue

        elif choice == 22:
            inverse = Inverse(current_matrix)
            continue

        elif choice == 23:
            rank = Rank(current_matrix)
            continue

        elif choice == 24:
            minimum = Minimum(current_matrix)
            continue

        elif choice == 25:
            maximum = Maximum(current_matrix)
            continue

        elif choice == 26:
            mean = Mean(current_matrix)
            continue

        elif choice == 27:
            median = Median(current_matrix)
            continue

        elif choice == 28:
            std = Standard_Deviation(current_matrix)
            continue

        elif choice == 29:
            rows = current_matrix.shape[0] 
            print(f"Enter {rows} numbers to append to matrix")
            elements = list(map(float, input().split()))
            if len(elements) != rows:
                raise ValueError("Number of elements does not match the number of rows")
            append_row = Append_To_Row(current_matrix, elements)
            continue

        elif choice == 30:
            columns = current_matrix.shape[1]
            print(f"Enter {columns} numbers to append to matrix")
            elements = list(map(float, input().split()))
            if len(elements) != columns:
                raise ValueError("Number of elements does not match the number of columns")
            append_column = Append_To_Column(current_matrix, elements)
            continue

        elif choice == 31:
            row = int(input("Enter the row index to delete: "))
            delete_row = Delete_Row(current_matrix, row)
            continue

        elif choice == 32:
            column = int(input("Enter the column index to delete: "))
            delete_column = Delete_Column(current_matrix, column)
            continue

        elif choice == 33:
            print("How do you want to input Matrix A")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_a = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_a = Load_Matrix(file_path)

            print("How do you want to input Matrix B")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_b = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_b = Load_Matrix(file_path)

            concat_row = Concatenate_Matrix_Row(matrix_a, matrix_b)
            continue

        elif choice == 34:
            print("How do you want to input Matrix A")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_a = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_a = Load_Matrix(file_path)

            print("How do you want to input Matrix B")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_b = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_b = Load_Matrix(file_path)

            concat_column = Concatenate_Matrix_Column(matrix_a, matrix_b)
            continue

        elif choice == 35:
            print("How do you want to input Matrix A")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_a = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_a = Load_Matrix(file_path)

            print("How do you want to input Matrix B")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_b = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_b = Load_Matrix(file_path)

            stack_row = Stack_Matrix_Row(matrix_a, matrix_b)
            continue

        elif choice == 36:
            print("How do you want to input Matrix A")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_a = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_a = Load_Matrix(file_path)

            print("How do you want to input Matrix B")
            print("1. Create Matrix")
            print("2. Load Matrix")
            matrixx = int(input("Enter your choice: "))
            if matrixx == 1:
                rows = int(input("Enter Number Of Rows: "))
                columns = int(input("Enter Number Of Columns: "))
                matrix_b = Create_Matrix(rows, columns)
            elif matrixx == 2:
                file_path = input("Enter file path: ")
                matrix_b = Load_Matrix(file_path)

            stack_column = Stack_Matrix_Column(matrix_a, matrix_b)
            continue

        elif choice == 37:
            row = int(input("Enter Row to split: "))
            splitrows = Split_Rows(current_matrix, row)
            continue

        elif choice == 38:
            column = int(input("Enter Column to split: "))
            splitcolumns = Split_Columns(current_matrix, column)
            continue

        elif choice == 39:
            null = Null_Matrix(current_matrix)
            continue



if __name__ == "__main__":
    main()