#!/usr/bin/env python3
"""
This script generates a plot of the graphical representaton of Men's Height vs Weight.
"""

import numpy as np
import matplotlib.pyplot as plt

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

plt.title("Men's Height vs Weight")
plt.xlabel('Height (in)')
plt.ylabel('Weight (lbs)')

plt.scatter(x, y, color='m')
plt.show()
