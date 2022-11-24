# 01_stammfunktion.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots(figsize=(6, 6))
plt.title(r'$s\left( t\right) =\int v\left( t\right)dt$')
plt.subplots_adjust(left=0.12, bottom=0.22)
plt.xlim(0, 5)
plt.ylim(0, 5.5)
plt.xlabel('t')
plt.ylabel('v, s')
t = np.arange(0, 5, 0.001)


def f(t, v=1):
    return 0 * t + v


def F(t, v=1):
    return v * t


fx, Fx = plt.plot(t, f(t), t, F(t))
fx.set(color='red', lw=2)
Fx.set(color='blue', lw=2)
# x-, y-Position, Laenge, Hoehe
xyA = plt.axes([0.1, 0.10, 0.8, 0.03])
# Slider-Objekt erzeugen
sldA = Slider(xyA, 'v', 0, 5.0, valinit=1, valstep=0.1)


def update(val):
    v = sldA.val
    fx.set_data(t, f(t, v))
    Fx.set_data(t, F(t, v))


# Aenderungen abfragen
sldA.on_changed(update)
ax.grid(True)
plt.show()
