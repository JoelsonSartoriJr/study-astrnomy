import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(0.1, 10, 1000)

fring= 2*np.sqrt(2) * u /np.power(u*u+1, 1.5)
fpunctual = 1.0/(u*u)

plt.plot(u, fring, "-", label="Ring")
plt.plot(u, fpunctual, "--", label="Punctual")

plt.axvline(1, color='black', linestyle='--')

plt.xlabel('distance')
plt.ylabel('Fg')

plt.legend(loc='best')
plt.ylim(0, 1.2)
plt.grid()

plt.savefig('exercises/graph/graph_exerc1.jpg')