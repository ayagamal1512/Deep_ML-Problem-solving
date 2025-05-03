# Batch Iterator for Dataset

# Implement a batch iterable function that samples in a numpy array X and an optional numpy array y. The function should yield batches of a specified size. If y is provided, the function should yield batches of (X, y) pairs; otherwise, it should yield batches of X only.

# Example:
# Input:
# X = np.array([[1, 2], 
#                   [3, 4], 
#                   [5, 6], 
#                   [7, 8], 
#                   [9, 10]])
#     y = np.array([1, 2, 3, 4, 5])
#     batch_size = 2
#     batch_iterator(X, y, batch_size)
# Output:
# [[[[1, 2], [3, 4]], [1, 2]],
#      [[[5, 6], [7, 8]], [3, 4]],
#      [[[9, 10]], [5]]]


import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    batches = []
    num_samples = X.shape[0]
    for i in range(0, num_samples, batch_size):
        end_idx = i + batch_size
        if y is not None:
            batches.append((X[i:end_idx,:], y[i:end_idx]))
        else:
            batches.append(X[i:end_idx,:])
    return batches