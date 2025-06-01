# Implement F-Score Calculation for Binary Classification

# Task: Implement F-Score Calculation for Binary Classification
# Your task is to implement a function that calculates the F-Score for a binary classification task. The F-Score combines both Precision and Recall into a single metric, providing a balanced measure of a model's performance.

# Write a function f_score(y_true, y_pred, beta) where:

# y_true: A numpy array of true labels (binary).
# y_pred: A numpy array of predicted labels (binary).
# beta: A float value that adjusts the importance of Precision and Recall. When beta=1, it computes the F1-Score, a balanced measure of both Precision and Recall.
# The function should return the F-Score rounded to three decimal places.

# Example:
# Input:
# y_true = np.array([1, 0, 1, 1, 0, 1])
# y_pred = np.array([1, 0, 1, 0, 0, 1])
# beta = 1

# print(f_score(y_true, y_pred, beta))
# Output:
# 0.857

import numpy as np

def f_score(y_true, y_pred, beta):
    """
    Calculate F-Score for a binary classification task.

    :param y_true: Numpy array of true labels
    :param y_pred: Numpy array of predicted labels
    :param beta: The weight of precision in the harmonic mean
    :return: F-Score rounded to three decimal places
    """
    TP = np.sum((y_pred == 1) & (y_true == 1))
    FN = np.sum((y_pred == 0) & (y_true == 1))
    FP = np.sum((y_pred == 1) & (y_true == 0))
    TN = np.sum((y_pred == 0) & (y_true == 0))
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    if precision + recall == 0:
        f_score_value = 0
    else:
        f_score_value = (1 + beta**2) * (precision * recall) / (beta**2 * precision + recall)
    return round(f_score_value, 3)

