from math import *
# If the exact root is given

def f(x):
    return (x**3) - 2 * (x**2) - 5

def f_derivative(x):
    return 3*(x**2) - 4 * x


def newtonRaphson(initialGuess, exactRoot, errorValue):
    x_n = initialGuess
    n = 0 # iteration counter

    while True:
        f_xn = f(x_n)
        f_derivative_xn = f_derivative(x_n)
        n += 1
        x_n1 = x_n - (f_xn / f_derivative_xn)
        print(f"Iteration:{n}, difference: {abs(exactRoot - x_n1)}")
        if abs(exactRoot - x_n1) < errorValue:
            break

        x_n = x_n1
    print(n)
    return x_n1

initialGuess = 2
errorValue = 10 ** (-4)
exactRoot = 2.69064744802878

result = newtonRaphson(initialGuess, exactRoot, errorValue)

print(f"Result is {result}")

