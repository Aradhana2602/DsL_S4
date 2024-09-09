def TransposeSparseMatrix(sp_r):
    row = sp_r[0][0]
    col = sp_r[0][1]
    non_ze = sp_r[0][2]

    tra_sp = []
    colt = [0] * col
    index = [0] * (col + 1)

    for i in range(1, non_ze + 1):
        colt[sp_r[i][1]] += 1

    index[0] = 1
    for i in range(1, col + 1):
        index[i] = index[i - 1] + colt[i - 1]

    tra_sp.append([col, row, non_ze])
    for i in range(1, non_ze + 1):
        x = index[sp_r[i][1]]
        tra_sp.append([sp_r[i][1], sp_r[i][0], sp_r[i][2]])
        index[sp_r[i][1]] += 1

    print("Transpose of sparse matrix:")
    for row in tra_sp:
        print(row)

def SimpleTranspose(sp_r):
    num_rows = sp_r[0][0]
    num_cols = sp_r[0][1]
    transposed = [[0] * num_rows for _ in range(num_cols)]

    for i in range(1, len(sp_r)):
        row, col, value = sp_r[i]
        transposed[col][row] = value

    return transposed

def AddSparse(sp1, sp2):
    r1, c1, n1 = sp1[0]
    r2, c2, n2 = sp2[0]

    if r1 != r2 or c1 != c2:
        print("Given matrices cannot be added")
        return []

    sp3 = [[r1, c1, 0]]

    i = 1
    j = 1
    while i <= n1 and j <= n2:
        if sp1[i][0] == sp2[j][0] and sp1[i][1] == sp2[j][1]:
            sp3.append([sp1[i][0], sp1[i][1], sp1[i][2] + sp2[j][2]])
            sp3[0][2] += 1
            i += 1
            j += 1
        elif sp1[i][0] == sp2[j][0]:
            if sp1[i][1] < sp2[j][1]:
                sp3.append(sp1[i])
                i += 1
            else:
                sp3.append(sp2[j])
                j += 1
            sp3[0][2] += 1
        else:
            if sp1[i][0] < sp2[j][0]:
                sp3.append(sp1[i])
                i += 1
            else:
                sp3.append(sp2[j])
                j += 1
            sp3[0][2] += 1

    while i <= n1:
        sp3.append(sp1[i])
        i += 1
        sp3[0][2] += 1

    while j <= n2:
        sp3.append(sp2[j])
        j += 1
        sp3[0][2] += 1

    return sp3

def insparse():
    row = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of columns: "))
    sp_r = [[row, col, 0]]

    non_ze = 0
    for i in range(row):
        print(f"Enter the elements of row {i + 1}:")
        for j in range(col):
            x = int(input())
            if x != 0:
                sp_r.append([i, j, x])
                non_ze += 1

    sp_r[0][2] = non_ze
    return sp_r

def outsparse(sp_r):
    print("Sparse matrix is:")
    for row in sp_r:
        print(row)

sp1 = insparse()
outsparse(sp1)

sp2 = insparse()
outsparse(sp2)

print("\nTranspose Sparse Matrix:")
TransposeSparseMatrix(sp1)

print("\nSimple Transpose:")
simple_transposed = SimpleTranspose(sp1)
for row in simple_transposed:
    print(row)

print("\nAddition of Sparse Matrices:")
added_sparse = AddSparse(sp1, sp2)
outsparse(added_sparse)








//polynomial2

def addPoly(p1, p2):
    # Determine the maximum length of the two polynomials
    max_len = max(len(p1), len(p2))
    
    # Initialize the resulting polynomial with zeros
    p3 = [0] * max_len
    
    # Add coefficients from p1
    for i in range(len(p1)):
        p3[i] += p1[i]
    
    # Add coefficients from p2
    for i in range(len(p2)):
        p3[i] += p2[i]
    
    return p3

def displayPoly(p):
    n = len(p)
    result = []
    
    for i in range(n):
        coeff = p[i]
        power = n - i - 1
        if coeff != 0:
            if result:
                result.append(f" + {coeff}x^{power}" if coeff > 0 else f" - {-coeff}x^{power}")
            else:
                result.append(f"{coeff}x^{power}")
    
    if not result:
        result.append("0")
    
    print("".join(result))

def getPolynomialInput():
    while True:
        try:
            input_str = input("Enter the polynomial coefficients as a list (e.g., [3, 7, 3, 1]): ")
            # Remove brackets and spaces, then convert to list of integers
            input_str = input_str.strip('[]').strip()
            coefficients = list(map(int, input_str.split(',')))
            return coefficients
        except ValueError:
            print("Invalid input. Please enter integers separated by commas.")

# Get polynomial inputs from the user
print("Enter the coefficients for polynomial p1 (e.g., [2, 0, 4, 0, 2, 4]):")
p1 = getPolynomialInput()

print("Enter the coefficients for polynomial p2 (e.g., [3, 7, 3, 1]):")
p2 = getPolynomialInput()

# Perform polynomial addition and display the result
result_poly = addPoly(p1, p2)
print("The resulting polynomial is:")
displayPoly(result_poly)

