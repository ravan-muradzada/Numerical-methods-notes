import numpy as np

def gaussionElimination(matrix, b):
    n, m = len(matrix), len(matrix[0])

    if n != m:
        print("Failed! Matrix should be square!")
        return None

    # Forward elimination
    for diagonal in range(n-1):
        if matrix[diagonal][diagonal] == 0:
            print("Failed! Matrix should not be singular!")
            return None
        
        for i in range(diagonal + 1, n):
            factor = matrix[i][diagonal] / matrix[diagonal][diagonal]

            for j in range(diagonal, n):
                matrix[i][j] -= factor * matrix[diagonal][j]
            b[i] -= factor * b[diagonal]


    # Back substitution
    resultsList = n * [0]
    resultsList[n-1] = b[n-1] / matrix[n-1][n-1]

    for i in range(n-2, -1, -1):
        sum = b[i]

        for j in range(i+1, n):
            sum -= resultsList[j] * matrix[i][j]

        resultsList[i] = sum / matrix[i][i]
    
    return resultsList

matrix = [
    [2, 3, -1],
    [0, 1, 4],
    [0, 0, 3]
]

b = [5, 6, 3]

result = gaussionElimination(matrix, b)

print(result)