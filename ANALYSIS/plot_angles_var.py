import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D # Required for 3D axes

data_MIL100 = [
    [0, 0, 1000],
    [0, 15, 1000],
    [0, 30, 1000],
    [0, 45, 1000],
    [0, 60, 1000],
    [0, 75, 1000],
    [15, 0, 1000],
    [15, 15, 1000],
    [15, 30, 1000],
    [30, 0, 1000],
    [30, 15, 1000],
    [45, 0, 1000]]

x = np.linspace(-90, 90, 13)
y = np.linspace(-90, 90, 13)

X, Y = np.meshgrid(x, y)
Z = np.ones((13, 13)) * -1.0
for i in range(13):
    for j in range(13):
        x = abs(-90 + i * 15)
        y = abs(-90 + j * 15)
        for rec in data_MIL100:
            if rec[0] == x and rec[1] == y:
                Z[i][j] = data_MIL100[0][2] - rec[2]
                break

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('θ')
ax.set_ylabel('φ')
ax.set_zlabel('∆E, Eh')

plt.show()