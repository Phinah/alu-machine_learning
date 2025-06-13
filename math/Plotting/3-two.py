
#!/usr/bin/env python3\
"""
This script generates a plot of the exponential decay of Carbon-14 and Radium-226 over time.
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

plt.plot(x, y1, 'r--', x, y2, 'g')
plt.title('Exponential Decay of Radioactive Elements')
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.legend(['c-14', 'Ra-226'])
plt.axis([0, 20000, 0, 1])
plt.show()
