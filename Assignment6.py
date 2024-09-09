def addPoly(p1, p2):
    max_len = max(len(p1), len(p2))
    
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
