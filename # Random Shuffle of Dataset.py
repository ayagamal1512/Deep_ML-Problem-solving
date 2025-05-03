# Random Shuffle of Dataset

# Write a Python function to perform a random shuffle of the samples in two numpy arrays, X and y, while maintaining the corresponding order between them. The function should have an optional seed parameter for reproducibility.

# Example:
# Input:
# X = np.array([[1, 2], 
#                   [3, 4], 
#                   [5, 6], 
#                   [7, 8]])
#     y = np.array([1, 2, 3, 4])
# Output:
# (array([[5, 6],
#                     [1, 2],
#                     [7, 8],
#                     [3, 4]]), 
#              array([3, 1, 4, 2]))




import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
    if seed is not None:
        np.random.seed(seed)
    indecies = np.random.permutation(len(X))
    X_shuffled = X[indecies]
    y_shuffled = y[indecies]
    
    return X_shuffled , y_shuffled