# 08_plot_geometrisch.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots(figsize=(8, 8))
plt.title(r'$a_{n}=a_{1}q^{n-1}$')
plt.subplots_adjust(left=0.12, bottom=0.25)
plt.ylim(-3, 3)
plt.xlabel('n')
plt.ylabel('$a_{n}$')
n = np.arange(1, 13, 1)


def f(n, a1, q):
    return a1 * q ** (n - 1)


y, = plt.plot(n, f(n, 2.5, -0.75), 'rx')

# x-, y-Position, Laenge, Hoehe
xyA = plt.axes([0.1, 0.10, 0.8, 0.03])
xyB = plt.axes([0.1, 0.05, 0.8, 0.03])
# Slider Objekte erzeugen
sldA = Slider(xyA, '$a_{1}$', 0.5, 2.5, valinit=2.5, valstep=0.1)
sldB = Slider(xyB, 'q', -1.0, 1.0, valinit=-0.75, valstep=0.01)


def update(val):
    a1 = sldA.val
    q = sldB.val
    y.set_data(n, f(n, a1, q))
    fig.canvas.draw_idle()


# Aenderungen abfragen
sldA.on_changed(update)
sldB.on_changed(update)
ax.grid(True)
plt.show()
