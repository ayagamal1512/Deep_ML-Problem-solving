# Linear Regression Using Gradient Descent

# Write a Python function that performs linear regression using gradient descent. The function should take NumPy arrays X (features with a column of ones for the intercept) and y (target) as input, along with learning rate alpha and the number of iterations, and return the coefficients of the linear regression model as a NumPy array. Round your answer to four decimal places. -0.0 is a valid result for rounding a very small number.

# Example:
# Input:
# X = np.array([[1, 1], [1, 2], [1, 3]]), y = np.array([1, 2, 3]), alpha = 0.01, iterations = 1000
# Output:
# np.array([0.1107, 0.9513])
# Reasoning:
# The linear model is y = 0.0 + 1.0*x, which fits the input data after gradient descent optimization.

#solution

import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    # Ensure input types
    X = np.array(X, dtype=np.float64)
    y = np.array(y, dtype=np.float64).reshape(-1, 1)

    # Add bias term (column of ones)
    m, n = X.shape 
    # Initialize theta (n+1, 1)
    theta = np.zeros((n, 1))

    # Gradient descent loop
    for _ in range(iterations):
        y_pred = X.dot(theta)
        gradient = (1 / m) * X.T.dot(y_pred - y)
        theta -= alpha * gradient

    # Return all theta values (intercept + slopes), rounded
    return np.round(theta.flatten(), 4).tolist()