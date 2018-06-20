import numpy as num
from scipy import stats
from matplotlib import pyplot as plt

x = num.array([1, 2, 3, 4, 5])
y = num.array([2, 1.8, 3, 3.2, 2.8])

plt.plot(x, y, 'ro', color='black')
plt.xlabel('Size of house')
plt.ylabel('Price')

plt.plot()
plt.show()