# 03_funkplot1.py

import numpy as np
import matplotlib.pyplot as plt

# Erzeugung eines 1-dimensionales Array vom Typ <class 'numpy.narray'>
# mit 500 Gleitpunktzahlen für den Wertebereich der unabhängigen Variablen x
x = np.linspace(0, 10, 500)
y = x ** 2

plt.plot(x, y, linewidth=2, linestyle='-', color='b')
plt.show()
