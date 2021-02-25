import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 1 # mean and standard deviation
X = np.random.normal(mu, sigma, 1000)
Y = X**2

plt.scatter(X, Y)
plt.show()
print(np.corrcoef(X, Y))