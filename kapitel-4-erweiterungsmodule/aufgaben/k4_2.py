import numpy as np
import matplotlib.pyplot as plt

# x-Werte
x = np.linspace(0, 360, 1000)

# mathematische Funktionen definieren
y1 = 10 * np.sin(2 * np.pi * x / 360.)
y2 = 10 * np.cos(2 * np.pi * x / 360.)

# Funktionsplot
fig, ax = plt.subplots(figsize=(10, 5))

ax.set_title("Sinus und Cosinus")
ax.plot(x, y1, 'b-', lw=1, label='$\sin x$')
ax.plot(x, y2, 'g-', lw=1, label='$\cos x$')
ax.set_xlabel('x')
ax.set_ylabel('y', rotation=True)
ax.legend(loc='best')

ax.set_xticks(np.arange(0, 361, 30))
ax.set_yticks(np.arange(-10, 11, 2))
ax.grid(True)
plt.show()
