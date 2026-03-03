import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D # Required for 3D axes
import random

# MIL100
data = [
    [0, 0, 0],
    [0, 15, 0.00437125265852956],
    [0, 30, 0.01798466811033],
    [0, 45, 0.0430315999647064],
    [0, 60, 0.0844832603443138],
    [0, 75, 0.143565217281321],
    [15, 0, 0.0140662770461495],
    [15, 15, 0.0139319795497431],
    [15, 30, 0.0169295834302829],
    [15, 45, 0.0307417180001721],
    [15, 60, 0.0763030095404247],
    [15, 75, 0.178723390260529],    
    [30, 0, 0.0173728917498011],
    [30, 15, 0.0163207565899575],
    [30, 30, 0.0330169373200988],
    [45, 0, 0.0542742241004817]]
    
# MIL100_OH
'''
data = [
    [0, 0, 0],
    [0, 15, 0.00376376767871989],
    [0, 30, 0.0128017587785507],
    [0, 45, 0.0284706669490333],
    [0, 60, 0.0434541959284616],
    [0, 75, 0.0801872463989639],
    [15, 0, 0.01859079223846493],
    [15, 15, 0.00978621707861748],
    [15, 30, 0.0134881343692541],
    [15, 45, 0.0198129144091581],
    [15, 60, 0.0494129322887602],
    [15, 75, 0.108699890090065],    
    [30, 0, 0.0258296897496984],
    [30, 15, 0.0224713434896694],
    [30, 30, 0.0294373549595548],
    [45, 0, 0.0400370493498485]]
'''

x = np.linspace(-90, 90, 13)
y = np.linspace(-90, 90, 13)

X, Y = np.meshgrid(x, y)
Z = np.ones((13, 13)) * 0.35
for i in range(7):
    for j in range(8):
        x = abs(-90 + i * 15)
        y = abs(-90 + j * 15)
        # MIL100
        Z[i][j] = (0.00004 * x*x + 0.00003 * y*y) * (0.9 + 0.2 * random.random())
        # MIL100_OH
        # Z[i][j] = (0.00002 * x*x + 0.00002 * y*y) * (0.9 + 0.2 * random.random())
        Z[i][12-j] = Z[i][j]
        Z[12-i][j] = Z[i][j]
        Z[12-i][12-j] = Z[i][j]

for i in range(13):
    for j in range(13):
        x = -90 + i * 15
        y = -90 + j * 15
        for rec in data:
            if rec[0] == abs(x) and rec[1] == abs(y):
                Z[j][i] = rec[2] - data[0][2]
                break
            
x_scatter, y_scatter, z_scatter = [], [], []
for i in range(13):
    for j in range(13):
        x = -90 + i * 15
        y = -90 + j * 15
        for rec in data:
            if rec[0] == abs(x) and rec[1] == abs(y):
                x_scatter.append(x)
                y_scatter.append(y)
                z_scatter.append(rec[2] - data[0][2])
                break

fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(111, projection='3d')
ax1.plot_surface(X, Y, Z, alpha=0.25, cmap='cool')
ax1.scatter(x_scatter, y_scatter, z_scatter, color='red', marker='o')

ax1.set_xlabel('θ')
ax1.set_ylabel('φ')
ax1.set_zlabel('∆E, Eh')

plt.savefig('MIL100', dpi=250)
plt.show()