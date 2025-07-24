import numpy as np

def Create_Matrix(rows, columns):
    while True:
        print("Select the type of matrix you want to create:")
        print("1. Identity Matrix")
        print("2. Zero Matrix")
        print("3. Random Matrix")
        print("4. Custom Matrix")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            matrix = np.eye(rows, columns)
            print(f"Identity Matrix of size {rows}x{columns}:\n{matrix}")
            return matrix
        elif choice == '2':
            matrix = np.zeros((rows, columns))
            print(f"Zero Matrix of size {rows}x{columns}:\n{matrix}")
            return matrix
        elif choice == '3':
            matrix = np.random.randint(0, 100, size=(rows, columns))
            print(f"Random Matrix of size {rows}x{columns}:\n{matrix}")
            return matrix
        elif choice == '4':
            print(f"Enter {rows * columns} elements row-wise (space separated):")
            elements = list(map(float, input().split()))
            if len(elements) != rows * columns:
                raise ValueError(f"Expected {rows * columns} elements, got {len(elements)}.")
            matrix = np.array(elements).reshape(rows, columns)
            return matrix
        else:
            print("Invalid choice. Please try again.")