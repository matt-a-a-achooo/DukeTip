import array as np
import matplotlib.pyplot as plt


x = [-40, -20, 0, 20, 40, 60, 80] # angle measurements
y = [61, 177.33,  296.33, 680.33, 651, 534.67, 24.67] # average


result = np.polyfit(x, y, 2)
print(result)
eq = np.poly1d(result)
print(eq)
print(eq(2))


x2 = np.arange(-40, 90) # gives a range for the angles
yfit = np.polyval(result, x2)
print(yfit)
plt.plot(x, y, label='Point')
plt.plot(x2, yfit, label='Fit')


user_input = raw_input("Enter Angle:") # asks user for an angle

mynumber=user_input

try:
    number = int(user_input) # prints answer based off of user input
except ValueError:
    print 'Exception Happened' #just in case user_input is not an integer
print eq(number)

