'''Implement Precision Metric

Write a Python function precision that calculates the precision metric given two numpy arrays: y_true and y_pred. The y_true array contains the true binary labels, and the y_pred array contains the predicted binary labels. Precision is defined as the ratio of true positives to the sum of true positives and false positives.

Example:
Input:
import numpy as np

y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])

result = precision(y_true, y_pred)
print(result)
Output:
1.0'''



#using for loop (ineefficient)

def precision(y_true, y_pred):
	# Your code here
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i] == 1:
            TP = TP +1 
        elif y_true[i] ==y_pred[i] == 0:
            TN = TN + 1 
        elif y_true[i] != y_pred[i] and y_true[i] == 0:
            FP = FP +1 
        elif y_true[i] != y_pred[i] and y_true[i] == 1:
            FN = FN + 1
        else:
            break 

    precision = TP / (TP + FP)
    return precision

#using numpy 

import numpy as np

def precision(y_true, y_pred):
    TP = np.sum((y_true == 1) & (y_pred == 1))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    
    if TP + FP == 0:
        return 0.0  # Avoid division by zero
    return TP / (TP + FP)