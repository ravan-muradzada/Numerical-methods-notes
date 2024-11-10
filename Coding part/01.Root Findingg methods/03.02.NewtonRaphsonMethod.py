from math import *
# If exact root is not give

def f(x):
    return (x**3) - 2 * (x**2) - 5

def f_derivative(x):
    return 3*(x**2) - 4 * x


def newtonRaphson(initialGuess, errorValue):
    x_n = initialGuess

    while True:
        f_xn = f(x_n)
        f_derivative_xn = f_derivative(x_n)

        x_n1 = x_n - (f_xn / f_derivative_xn)

        if abs(x_n - x_n1) < errorValue:
            break

        x_n = x_n1

    return x_n1

initialGuess = 2
errorValue = 10 ** (-4)

result = newtonRaphson(initialGuess, errorValue)

print(f"Result is {result}")

