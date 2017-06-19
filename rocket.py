import numpy as np
import matplotlib.pyplot as plt


x = [-40, -20, 0, 20, 40, 60, 80]
y = [61, 177.33,  296.33, 680.33, 651, 534.67, 24.67]


result = np.polyfit(x, y, 2)
print(result)
eq = np.poly1d(result)
print(eq)
print(eq(2))


x2 = np.arange(-40, 90)
yfit = np.polyval(result, x2)
print(yfit)
plt.plot(x, y, label='Point')
plt.plot(x2, yfit, label='Fit')
plt.show()

user_input = raw_input("Enter Angle:")

mynumber=user_input

try:
    number = int(user_input)
except ValueError:
    print 'Exception Happened'
print eq(number)

