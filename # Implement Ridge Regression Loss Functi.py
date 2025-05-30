# Implement Ridge Regression Loss Function

# Write a Python function ridge_loss that implements the Ridge Regression loss function. The function should take a 2D numpy array X representing the feature matrix, a 1D numpy array w representing the coefficients, a 1D numpy array y_true representing the true labels, and a float alpha representing the regularization parameter. The function should return the Ridge loss, which combines the Mean Squared Error (MSE) and a regularization term.

# Example:
# Input:
# import numpy as np

# X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
# w = np.array([0.2, 2])
# y_true = np.array([2, 3, 4, 5])
# alpha = 0.1

# loss = ridge_loss(X, w, y_true, alpha)
# print(loss)
# Output:
# 2.204

'''solution'''

import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	m = X.shape[0]
	y_pred = np.dot(X,w) 
	loss = 1/m * sum((y_pred - y_true)**2 )+ alpha * sum(w**2)
	return round(loss,3) 
