import numpy as np
import matplotlib.pyplot as plt
from velocidade_bojo_disco_halo import vd, vb


df = np.loadtxt('dados/m31.dat', dtype=float).transpose()
plt.errorbar(df[0], df[1], fmt='o', label="Observado")

rmax= 1000 #kpc

r = np.linspace(0.1, rmax, 10000)

#valores possiveis
Vb = vb(r, 0.1, 0.6e10)
Vd = vd(r, 8.0, 4.0e10)

V = np.sqrt(Vb*Vd + Vb*Vd)

plt.plot(r, Vb, "--", label="Bojo")
plt.plot(r, Vd, "--", label="Disco")
plt.plot(r, V, "-", lw=2, label="Bojo + Disco")

plt.margins(0.1)
plt.xlim(0,rmax)
plt.ylim(0,300)
plt.title(u"Curva de rotação de M31")
plt.xlabel(u"Raio (kpc)")
plt.ylabel(u"Velocidade (km/s)")
plt.legend(loc="upper right")
plt.grid()
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.96, top=0.9)
plt.show()