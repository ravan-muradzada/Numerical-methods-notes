from math import *
# If exact root is not give

def f(x):
    return sin(x) - (x/2)

def f_derivative(x):
    return cos(x) - 0.5

def newtonRaphson(initialGuess, errorValue):
    x_n = initialGuess
    x_n1 = 0
    
    while True:
        f_xn = f(x_n)
        f_derivative_xn = f_derivative(x_n)
        
        if f_derivative_xn == 0:
            print("Derivative is zero, method fails!")
            return None

        x_n1 = x_n - (f_xn / f_derivative_xn)

        if abs(x_n1 - x_n) < errorValue:
            break

        x_n = x_n1

    return x_n1

initialGuess = 1.5
errorValue = 0.0001

result = newtonRaphson(initialGuess, errorValue)

print(f"Result is {result}")