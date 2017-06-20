import numpy as np #imports numpy

onesM = np.ones((4, 5)) # creates a 5 by 4 array
zeros = np.zeros((1, 5)) # creates a 5 by 1 array
print(onesM)
twos = zeros
twos[0,0] = 1 # prints a 1 in the 0 index then the rest are o
print(twos)
print onesM * zeros # multiples 5by4 and the 5by1
onesM[1, 2] = 10 # replaces 3rd number in the second row to 10
print(onesM)
print onesM * 2 #print the 5by4 times 2
print(onesM.sum()) # adds everything
print(onesM.sum(axis=0))
print(onesM.sum(axis=1))