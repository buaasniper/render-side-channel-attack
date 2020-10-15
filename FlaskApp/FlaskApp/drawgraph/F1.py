import numpy as np


TP = np.fromstring('17 16 17 19 17 11 20 16 17 17 17 11 20 15 12 13 16 12 14 17 19 19 19 20 19 18 11 19 17 11 20 20 11 12 20 16 17 18 16 14 16 15 11 20 14 11 14 13 20 16 20 14 19 15 18 16 12 12 17 15 19 17 12 18 20 13 12 20 15 11 15 20 17 20 16 18 15 16 17 14 13 13 14 16 20 12 12 14 14 15 13 11 20 15 15 20 18 12 17 11', dtype=int, sep=' ')
TN = np.fromstring('16 10 10 13 10 14 10 10 20 18 10 15 16 20 20 18 11 14 15 11 17 15 11 14 13 12 11 12 11 12 12 14 10 20 10 13 15 20 14 17 19 10 16 18 19 15 16 10 16 10 19 16 13 14 11 19 13 12 10 14 14 11 18 16 15 11 15 10 17 13 15 11 10 13 12 12 15 16 13 18 12 11 14 10 14 17 20 11 17 17 10 12 11 13 16 13 14 15 19 17', dtype=int, sep=' ')
FN = 20 - TP
FP = 20 - TN
precision = TP/(TP +FP)
recall = TP/(TP+FN)
F1 = (2 * precision * recall)/(precision + recall)
print(precision)
print(recall)
print(F1)


print(np.mean(precision))
print(np.mean(recall))
print(np.mean(F1))