import numpy as np

# Given data

x = np.array([1, 1.5, 1.6, 2.5, 3.5], dtype=float)
y = np.array([0.6767, 0.3734, 0.3261, 0.08422, 0.01596], dtype=float)

#----------------------------------------------------#
# Define the function and its true derivative

def f(x):
    return 5 * np.exp(-2 * x) * x

def true_derivative(x):
    return np.exp(-2 * x) * (5 - 10 * x)

#----------------------------------------------------#
# Numerical Differentiation Methods

def forward_difference(i):
    if i < len(x) - 1:  
        return (y[i+1] - y[i]) / (x[i+1] - x[i])
    else:
        return np.nan  # Not applicable for the last point

def backward_difference(i):
    if i > 0:  
        return (y[i] - y[i-1]) / (x[i] - x[i-1])
    else:
        return np.nan  # Not applicable for the first point

def central_difference(i):
    if i > 0 and i < len(x) - 1:  
        return (y[i+1] - y[i-1]) / (x[i+1] - x[i-1])
    else:
        return np.nan  # Not applicable for the first or last points

def calculate_true_percent_relative_error(exact, approx):
    return np.abs((exact - approx) / exact) * 100


print()
for i in range(len(x)):
    true_val = true_derivative(x[i])
    forward_val = forward_difference(i)
    backward_val = backward_difference(i)
    central_val = central_difference(i)
    
    forward_error = calculate_true_percent_relative_error(true_val, forward_val)
    backward_error = calculate_true_percent_relative_error(true_val, backward_val)
    central_error = calculate_true_percent_relative_error(true_val, central_val)
    
    print(f"x={x[i]}")
    print(f"Exact Derivative: {true_val:.3f}")
    print(f"Forward Difference: {forward_val:.3f}, Error: {forward_error:.3f}%")
    print(f"Backward Difference: {backward_val:.3f}, Error: {backward_error:.3f}%")
    print(f"Central Difference: {central_val:.3f}, Error: {central_error:.3f}%\n")
