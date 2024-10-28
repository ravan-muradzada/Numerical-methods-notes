import numpy as np
# It is naive version of Partial pivoting method, so here we swap the rows

def gaussianMethodUsingPartialPivoting(matrix, b):
    n, m = len(matrix), len(matrix[0])

    if n != m:
        print("Failed! Matrix should be square!")
        return None
    
    # Forward elimination
    for k in range(n):
        
        # Swapping rows
        for p in range(k+1, n):
            if abs(matrix[k][k]) < abs(matrix[p][k]):
                matrix[k], matrix[p] = matrix[p], matrix[k]
        
        if matrix[k][k] == 0:
            print("Failed! Division by zero!")
            return None
        
        for i in range(k+1, n):
            factor = matrix[i][k] / matrix[k][k]

            for j in range(k, n):
                matrix[i][j] -= factor * matrix[k][j]
            b[i] -= factor * b[k]
    
    # Back substition

    resulsList = n * [0]
    resulsList[n-1] = b[n-1] / matrix[n-1][n-1]

    for i in range(n-2, -1, -1):
        sum = b[i]

        for j in range(i+1, n):
            sum -= matrix[i][j] * resulsList[j]
        
        resulsList[i] = sum / matrix[i][i]
    
    return resulsList

matrix = [
    [2, 3, -1],
    [0, 1, 4],
    [0, 0, 3]
]

b = [5, 6, 3]

result = gaussianMethodUsingPartialPivoting(matrix, b)

print(result)