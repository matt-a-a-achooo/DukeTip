import numpy as np

onesM = np.ones((4, 5))
zeros = np.zeros((1, 5))
print(onesM)
twos = zeros
twos[0,0] = 1
print(twos)
print onesM * zeros
onesM[1, 2] = 10
print(onesM)
print onesM * 2
print(onesM.sum())
print(onesM.sum(axis=0))
print(onesM.sum(axis=1))