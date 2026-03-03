import matplotlib.pyplot as plt
import numpy as np

data_MIL100 = [
    [0, 0],
    [15, 0.0140662770461495],
    [30, 0.0173728917498011],
    [45, 0.0542742241004817]]

data_MIL100_OH = [    
    [0, 0],
    [15, 0.01859079223846493],
    [30, 0.0258296897496984],
    [45, 0.0400370493498485]]

x = np.linspace(-45, 45, 7)
y_MIL100 = [data_MIL100[abs(3 - i)][1] for i in range(7)]
data_MIL100_OH = [data_MIL100_OH[abs(3 - i)][1] for i in range(7)]

plt.plot(x, y_MIL100, color='black', label='MIL100')
plt.scatter(x, y_MIL100, color='black')
plt.plot(x, data_MIL100_OH, color='red', label='MIL100 OH')
plt.scatter(x, data_MIL100_OH, color='red')
plt.xlabel('θ')
plt.ylabel('∆E, Eh')
plt.legend()
plt.savefig('thetta_scan')
plt.show()
