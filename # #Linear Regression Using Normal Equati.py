# #Linear Regression Using Normal Equation

# Write a Python function that performs linear regression using the normal equation. The function should take a matrix X (features) and a vector y (target) as input, and return the coefficients of the linear regression model. Round your answer to four decimal places, -0.0 is a valid result for rounding a very small number.

# Example:
# Input:
# X = [[1, 1], [1, 2], [1, 3]], y = [1, 2, 3]
# Output:
# [0.0, 1.0]
# Reasoning:
# The linear model is y = 0.0 + 1.0*x, perfectly fitting the input data.#

#solution
import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
    X = np.array(X)
    y= np.array(y).reshape(-1,1)

    X_b = np.c_[np.ones((X.shape[0],1)),X]
    theta = np.linalg.pinv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    theta = np.round(theta,1).flatten().tolist()
    return [theta[0]+theta[1]]+theta[2:] 