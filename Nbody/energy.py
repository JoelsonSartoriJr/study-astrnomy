import numpy as np

def energy(pos:float, vel:float, mass:float, G:float)->float:
    """
        kinetic energy (KE) and potential energy (PE)
    """
    # Kinetic Energy:
    KE = 0.5 * np.sum(np.sum( mass * vel**2 ))

    x, y, z = pos[:,0:1], pos[:,1:2], pos[:,2:3]
    
    dx = x.T - x
    dy = y.T - y
    dz = z.T - z
    
    #stores 1/r for all particle pairwise particle separations
    inv_r = np.sqrt(dx**2 + dy**2 + dz**2)
    inv_r[inv_r>0] = 1.0/inv_r[inv_r>0]

    # sum over upper triangle, to count each interaction only once
    PE = G * np.sum(np.sum(np.triu(-(mass*mass.T)*inv_r,1)))

    return KE, PE