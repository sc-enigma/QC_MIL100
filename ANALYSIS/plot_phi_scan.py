import matplotlib.pyplot as plt
import numpy as np

data_MIL100 = [
    [0, 0],
    [15, 0.00437125265852956],
    [30, 0.01798466811033],
    [45, 0.0430315999647064],
    [60, 0.0844832603443138],
    [75, 0.143565217281321]]
    
data_MIL100_OH = [    
    [0, 0],
    [15, 0.00376376767871989],
    [30, 0.0128017587785507],
    [45, 0.0284706669490333],
    [60, 0.0434541959284616],
    [75, 0.0801872463989639]]

x = np.linspace(-75, 75, 11)
y_MIL100 = [data_MIL100[abs(5 - i)][1] for i in range(11)]
data_MIL100_OH = [data_MIL100_OH[abs(5 - i)][1] for i in range(11)]

plt.plot(x, y_MIL100, color='black', label='MIL100')
plt.scatter(x, y_MIL100, color='black')
plt.plot(x, data_MIL100_OH, color='red', label='MIL100 OH')
plt.scatter(x, data_MIL100_OH, color='red')
plt.xlabel('φ')
plt.ylabel('∆E, Eh')
plt.legend()
plt.savefig('phi_scan')
plt.show()