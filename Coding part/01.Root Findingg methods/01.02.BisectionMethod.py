from math import *

def function(x):
    return (x**3) - (7 * (x**2)) + 14 * x - 6

def bisectionMethod(lowerBound, upperBound, errorValue):
    if function(lowerBound) * function(upperBound) >= 0:
        print("Bisection method has failed!")
        return None
    n = 0 # iteration counter

    while ((upperBound - lowerBound) / 2) >= errorValue:
        mid = (upperBound + lowerBound) / 2.0
        n += 1

        print(f"Iteration:{n}\tCurrent Boundaries:\t[{lowerBound}, {upperBound}], mid is {mid} and f(mid) = {function(mid)}")
        # If it is needed we can print each time something like this

        if function(mid) == 0:
            # mid is exact value
            break
        elif function(lowerBound) * function(mid) > 0:
            lowerBound = mid
        else:
            upperBound = mid

    return (lowerBound + upperBound) / 2.0

lowerBound, upperBound = 0, 1
errorValue = 0.01

result = bisectionMethod(lowerBound, upperBound, errorValue)

print(f"\n\nResult is {result}")
