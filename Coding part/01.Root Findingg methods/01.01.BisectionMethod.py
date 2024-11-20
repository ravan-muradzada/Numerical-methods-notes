from math import *

def function(x):
    return (x**3) - (7 * (x**2)) + 14 * x - 6

def bisectionMethod(lowerBound, upperBound, exactValue, errorValue):
    if function(lowerBound) * function(upperBound) >= 0:
        print("Bisection method has failed!")
        return None
    n = 0 # iteration count

    while True:
        currentValue = (lowerBound + upperBound) / 2.0
  

        if function(currentValue) == 0:
            # currentValue is exact root
            break
        elif function(currentValue) * function(lowerBound) > 0:
            # Checking IVT each iteration
            lowerBound = currentValue
        else:
            upperBound = currentValue

        if abs(exactValue - currentValue) < errorValue:
            # If the current error value is less that given error value,
            # that means, we should stop the process.
            break

    return currentValue

lowerBound, upperBound = 0, 1
exactValue = 2 - sqrt(2)
errorValue = 0.01

result = bisectionMethod(lowerBound, upperBound, exactValue, errorValue)

print(f"\n\nThe result is {result}")