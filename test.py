import numpy as np

onesM = np.ones((5, 4))
ones = np.ones(4)
print(onesM)
print(ones)
twos = ones * 2
twos[0] = 0
print(twos)
print(onesM * twos)

print(onesM.sum())
print(onesM.sum(axis=1))
print(onesM.sum(axis=0))

random = np.random.rand(4, 4) * 10
print(random)
print(random.max())
random[1][:] = 11
random [2][3] = 11
random[:][3] = 12
print(random.argmax())
print(np.where(random==random.max()))