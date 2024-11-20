from math import *

def f(x):
    return (exp(x) / x) - (sin(x) / (x**2)) + 2 * x - 10

def secant(x0, x_1, errorValue):
    xn = x0
    xn_1 = x_1

    # xn means x(n) 1
    # xn_1 means x(n-1) 0
    # xn1 means x(n+1) 2

    while True:
        f_xn = f(xn)
        f_xn_1 = f(xn_1)

        xn1 = xn - ((f_xn * (xn_1 - xn)) / (f_xn_1 - f_xn))

        if abs(xn1 - xn) < errorValue:
            break

        xn_1 = xn
        xn = xn1

    return xn1

x0 = 1
x1 = 2
errorValue = 10 ** (-7)
res = secant(x0, x1, errorValue)

print(res)
