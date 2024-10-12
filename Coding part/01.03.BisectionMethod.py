from math import *
# Question: find sqrt(7) value

'''Solution:
    We x^2 = 7
    f(x) = x^2 - 7
    We need to implement algorithm for that function.
'''
def function(x):
    return x * x - 7

def bisectionMethod(low, high, errorValue):
    if function(low) * function(high) >= 0:
        print("Bisection method has failed!")
        return None

    n = 0 # iteration counter

    while ((high - low) / 2) >= errorValue:
        mid = (low + high) / 2.0
        n += 1

        print(f"Iteration: {n}, Boundaries: [{low}, {high}], mid = {mid}, f(mid) = {function(mid)}")
        # If it is needed

        if function(mid) == 0:
            # mid is exact value
            break
        elif function(low) * function(mid) > 0:
            low = mid
        else:
            high = mid

    return (low + high) / 2.0

errorValue = 10 ** (-15)
lowerBound, upperBound = 2, 3

result = bisectionMethod(lowerBound, upperBound, errorValue)

print(f"\n\nResult: {result}")
print(f"\n{result * result}")