# Implement Gini Impurity Calculation for a Set of Classes

# Task: Implement Gini Impurity Calculation
# Your task is to implement a function that calculates the Gini Impurity for a set of classes. Gini impurity is commonly used in decision tree algorithms to measure the impurity or disorder within a node.

# Example:
# Input:
# y = [0, 1, 1, 1, 0]
# print(gini_impurity(y))
# Output:
# 0.48



import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	num_classes = np.unique(y)
	N= len(y)
	p_sum = 0 
	for c in num_classes:
		p_c = np.sum(y==c) / N
		p_sum = p_sum + p_c**2

	val= 1- p_sum

	return round(val,3)