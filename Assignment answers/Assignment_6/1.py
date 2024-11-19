import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def function(x, a, b, c):
    return a * np.cos(x) + b * np.exp(x) + c

def solution_1(x, y):
    n = len(x)

    matrix = np.array([[sum(np.cos(x)**2), sum(np.cos(x)*np.exp(x)), sum(np.cos(x))], 
            [sum(np.cos(x)*np.exp(x)), sum(np.exp(2*x)), sum(np.exp(x))],[sum(np.cos(x)), sum(np.exp(x)), n]])

    right_hand_side = np.array([sum(y*np.cos(x)), sum(y*np.exp(x)), sum(y)])
    
    print("\nMatrix (left-hand side):\n")
    for i in matrix:
        print(i)
    print("\n\n")

    print("Right-hand side:\n")
    for i in right_hand_side:
        print(i, end="  ")
    print("\n\n\n\n")

    result_list = np.linalg.solve(matrix, right_hand_side)

    return result_list

def solution_2(x, y):
    result_list = curve_fit(function, x, y)[0]

    return result_list

def sketch_graph(x, y, predicated_values_for_y, xn, yn):
    plt.scatter(x, y, label="data")
    plt.plot(x, predicated_values_for_y, label="least squares")
    plt.grid()
    plt.legend()
    plt.plot(xn, yn, "*r")
    plt.show()


# Inputs
x = np.array([-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5])
y = np.array([-1, -0.7, 0.2, 1.5, 2.1, 3.2, 3.5, 3.6, 3.3, 
              3.6, 4.2, 5.7])


# Solution using Ax=B. In this function, parameters are printed
result_list_1 = solution_1(x, y)
print(f"Solution from solution 1:\n{result_list_1}\n\n")


# Solution using curve_fit function
result_list_2 = solution_2(x, y)
print(f"Solution from solution 2:\n{result_list_2}\n\n")


# Predicted values for y
predicated_values_for_y = function(x, *result_list_2)


# Finding residuals
residuals = abs(predicated_values_for_y - y)
print(f"Residuals: {residuals}")


# Giving a value
xn = 1.2
yn = function(xn, *result_list_2)


#Sketching graph
sketch_graph(x, y, predicated_values_for_y, xn, yn)