from velocidade_bojo_disco_halo import vb
import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0.01, 100, 1000)

plt.plot(r, vb(r, 2.0, 1e10), "b-", label= "$a_b = 2 Kpc, M_b = 10^{10} M_\\odot$")
plt.plot(r, vb(r, 5.0, 1e10), "r-", label= "$a_b = 5 Kpc, M_b = 10^{10} M_\\odot$")
plt.plot(r, vb(r, 2.0, 1e11), "b--", label= "$a_b = 2 Kpc, M_b = 10^{10} M_\\odot$")
plt.plot(r, vb(r, 5.0, 1e11), "r--", label= "$a_b = 5 Kpc, M_b = 10^{11} M_\\odot$")

plt.xlabel(u"Raio (Kpc)")
plt.ylabel(u"Velocidade (km/s)")

plt.xlim(0, 40)
plt.legend(loc="upper right")
plt.grid()
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.96, top=0.97)
plt.savefig('bojo.jpg')