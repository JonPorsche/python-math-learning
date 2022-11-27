# 05_plot_konvergenz.py
from math import *
import matplotlib.pyplot as plt

n = 10
summe = 0
for k in range(0, n + 1):
    summe = summe + 1 / factorial(k)
    plt.scatter(k, summe, marker='x', color='r')
plt.hlines(exp(1), 0, 10, color='black', ls='dashed')
plt.title(r'$\sum^{\infty }_{k=0} \frac{1}{k!} $')
plt.xlabel('k')
plt.ylabel('Summe')
plt.show()
