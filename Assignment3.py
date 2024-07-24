def main_menu():
    print("Welcome to the Menu")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Check Matrix Properties")
    print("5. Sum of Diagonal Elements")
    print("6. To Find Saddle Point")
    print("7. Exit")
    print()

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error: Matrices must have the same dimensions for addition.")
        return None
    
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def sub_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error: Matrices must have the same dimensions for subtraction.")
        return None
    
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    return result

def prod_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Error: Number of columns in matrix1 must be equal to number of rows in matrix2 for multiplication.")
        return None
    
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))] 
    for i in range(len(matrix1)):      
        for j in range(len(matrix2[0])):          
            for k in range(len(matrix2)):              
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def check_upper_triangular(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i < j and matrix[i][j] != 0:
                return False
    return True

def check_lower_triangular(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i > j and matrix[i][j] != 0:
                return False
    return True

def check_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i != j and matrix[i][j] != 0:
                return False
    return True

def sum_diagonal(matrix):
    sum_diag = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                sum_diag += matrix[i][j]
    return sum_diag
def saddle_point(matrix):
    m=len(matrix)
    n=len(matrix[0])
    for i in range(m):
 
 
        min_row = matrix[i][0]
        col_ind = 0
        for j in range(1, m):
            if (min_row > matrix[i][j]):
                min_row = matrix[i][j]
                col_ind = j
 
 
        k = 0
        for k in range(n):
 
 
            if (min_row < matrix[k][col_ind]):
                break
            k += 1
 
        if (k == n):
            return min_row
 

# Matrix input function
def input_matrices(num_matrices):
    matrices = []
    for _ in range(num_matrices):
        m = int(input("Enter the number of rows for matrix: "))
        n = int(input("Enter the number of columns for matrix: "))
        
        matrix = []
        print("Enter values for matrix ({}x{}):".format(m, n))
        for i in range(m):
            row = []
            for j in range(n):
                row.append(int(input("Enter the value for row {}, column {}: ".format(i+1, j+1))))
            matrix.append(row)
        matrices.append(matrix)
    return matrices

# Main program
def matrix_operations():
    num_matrices = int(input("Enter the number of matrices: "))
    matrices = input_matrices(num_matrices)
    
    while True:
        main_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':  # Add matrices
            if len(matrices) < 2:
                print("Error: Need at least 2 matrices for addition.")
                continue
            result = matrices[0]
            for matrix in matrices[1:]:
                result = add_matrices(result, matrix)
            print("Result of addition:", result)
        
        elif choice == '2':  # Subtract matrices
            if len(matrices) < 2:
                print("Error: Need at least 2 matrices for subtraction.")
                continue
            result = matrices[0]
            for matrix in matrices[1:]:
                result = sub_matrices(result, matrix)
            print("Result of subtraction:", result)
        
        elif choice == '3':  # Multiply matrices
            if len(matrices) < 2:
                print("Error: Need at least 2 matrices for multiplication.")
                continue
            result = matrices[0]
            for matrix in matrices[1:]:
                result = prod_matrices(result, matrix)
            print("Result of multiplication:", result)
        
        elif choice == '4':  # Check matrix properties
            for matrix in matrices:
                if check_upper_triangular(matrix):
                    print("Matrix is upper triangular.")
                elif check_lower_triangular(matrix):
                    print("Matrix is lower triangular.")
                elif check_diagonal(matrix):
                    print("Matrix is diagonal.")
                else:
                    print("Matrix is neither upper triangular, lower triangular, nor diagonal.")
        
        elif choice == '5':  # Sum of diagonal elements
            for matrix in matrices:
                print("Sum of diagonal elements:", sum_diagonal(matrix))

        elif choice == '6':  # Find saddle point
            for i, matrix in enumerate(matrices):
                s = saddle_point(matrix)
                if s == 0:
                    print(f"Matrix {i+1} does not have a saddle point.")
                else:
                    print(f"Saddle point of Matrix {i+1}: {s}")   
        
        elif choice == '7':  # Exit
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

# Run the program
matrix_operations()



