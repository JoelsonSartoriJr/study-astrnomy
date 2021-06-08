import numpy as np

def acceleration(pos:float, mass:float, G:float, softening:float)->float:
    """
        Calculate the acceleration on each particle due to Newton's Law 
    """
    x, y, z = pos[:,0:1], pos[:,1:2], pos[:,2:3]
    
    dx = x.T - x
    dy = y.T - y
    dz = z.T - z
    
    #1/r^3 for all
    inv_r3 = (dx**2 + dy**2 + dz**2 + softening**2)
    inv_r3[inv_r3>0] = inv_r3[inv_r3>0]**(-1.5)
    
    ax = G * (dx * inv_r3) @ mass
    ay = G * (dy * inv_r3) @ mass
    az = G * (dz * inv_r3) @ mass
    
    a = np.hstack((ax,ay,az))

    return a