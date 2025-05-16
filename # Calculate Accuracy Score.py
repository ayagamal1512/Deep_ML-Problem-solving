# Calculate Accuracy Score

# Write a Python function to calculate the accuracy score of a model's predictions. The function should take in two 1D numpy arrays: y_true, which contains the true labels, and y_pred, which contains the predicted labels. It should return the accuracy score as a float.

# Example:
# Input:
# y_true = np.array([1, 0, 1, 1, 0, 1])
#     y_pred = np.array([1, 0, 0, 1, 0, 1])
#     output = accuracy_score(y_true, y_pred)
#     print(output)
# Output:
# # 0.8333333333333334

#solution: 

import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	num_corr_pred = 0
	for i in range (len(y_pred)):
		if y_pred[i] == y_true[i]:
			num_corr_pred +=1
		else:
			num_corr_pred = num_corr_pred
	accuracy = num_corr_pred / len(y_pred)

	return accuracy 

#another solution


# def accuracy_score(y_true, y_pred):
# 	accuracy= np.mean(y_true == y_pred)
#     return accuracy

