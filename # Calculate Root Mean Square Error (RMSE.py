# Calculate Root Mean Square Error (RMSE)

# Task: Compute Root Mean Square Error (RMSE)
# In this task, you are required to implement a function rmse(y_true, y_pred) that calculates the Root Mean Square Error (RMSE) between the actual values and the predicted values. RMSE is a commonly used metric for evaluating the accuracy of regression models, providing insight into the standard deviation of residuals.

# Your Task:
# Implement the function rmse(y_true, y_pred) to:

# Calculate the RMSE between the arrays y_true and y_pred.
# Return the RMSE value rounded to three decimal places.
# Ensure the function handles edge cases such as:
# Mismatched array shapes.
# Empty arrays.
# Invalid input types.



import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	y_true = np.array(y_true).flatten()
	y_pred = np.array(y_pred).flatten()

	m= len(y_true)
	rmse_res = np.sqrt((1/m)*(np.sum((y_true - y_pred)**2))) 
	return round(rmse_res,3)
