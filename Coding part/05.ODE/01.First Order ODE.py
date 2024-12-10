# My code
import numpy as np

def f(x, y):
    return 1 + x*x

def taylor_series_method(x0, y0, delta, target):
    x, y = x0, y0

    x_values = np.arange(x0, target, delta)
    y_values = np.zeros(len(x_values))
    y_values[0] = y0

    for i in range(1, len(x_values)):
        x, y = x_values[i-1], y_values[i-1]

        y_values[i] = y + delta * f(x, y)

    return x_values, y_values

x0, y0 = 1, -4
target = 1.02
delta = 0.01

x_values, y_values = taylor_series_method(x0, y0, delta, target)


print(y_values[-1])