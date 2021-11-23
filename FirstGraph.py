from numpy import *
import matplotlib.pyplot as plt
import pylab

x = linspace(0,10)
y = x**cos(x**2)
plt.plot(x, y, 'g--', label='(x^cos(x^2))')

plt.xlabel('x')
plt.ylabel('y')
plt.title('First Graph')
plt.legend(["x^cos(x^2)"])

plt.show
pylab.show()