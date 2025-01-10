# If not already installed, install matplotlib using: pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_facecolor('lightgray')

x = np.linspace(0, 10, 100)
y = np.sin(x)

ax.plot(x, y, color='darkblue', lw=2)
ax.fill_between(x, y, color='skyblue', alpha=0.5)

plt.show()
