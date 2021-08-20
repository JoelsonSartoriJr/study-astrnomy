import math
import numpy as np
from scipy import integrate


def triple_integral(f, lim:list, k:int, args:tuple):
    """ Use Romberg integration to integrate a 3 variable function.
        
        \int_zi^2f \int_yi^yf \int_xi^xf f(x, y, z, args) dx dy dz

        Args:
            k: number points in dimensions N = 2**k +1
            f: function integration
            lim: limit integration.
            args: parameters function
            
        Returns:
            None
        
        Raises:
            None
    """
    
    N = 2**k + 1 # points integration
    X = np.linspace(lim[0], lim[1], N)
    Y = np.linspace(lim[2], lim[3], N)
    Z = np.linspace(lim[4], lim[5], N)
    
    dX = math.fabs(X[1]-X[0])
    dY = math.fabs(Y[1]-Y[0])
    dZ = math.fabs(Z[1]-Z[0])
    
    Iz = np.zeros(N)
    Iyz = np.zeros(N)
    Fxyz = np.zeros(N)
    
    for i in range(N):
        Ixy = np.zeros(N)
        for j in range(N):
            for k in range(N):
                Fxyz[k] = f(X[i], Y[j], Z[k], args)
            Iyz[j] = integrate.romb(Fxyz, dx=dX)
        Iz[i] = integrate.romb(Iyz, dx=dY)
    return integrate.romb(Iz, dx=dZ)

if __name__ == '__main__':
    def funcao(x, y, z, A):
        return math.exp(x+A*y+z)
    
    i = triple_integral(funcao, [-3, -2, 1, 2, 0, 1], 3, args=(-1.0))
    
    iexactly = (math.e-1)**3/math.e**5
    error = math.fabs(i-iexactly)/iexactly*100
    print(i, error)