import numpy as np
import matplotlib.pyplot as plt

from acceleration import acceleration
from energy import energy

def main():
    """ Init simulation N-body parameters"""
    
    N            = 100  # Number of particles
    t            = 0    # Time of the simulation
    tEnd         = 10.0 # time at which simulation ends
    dt           = 0.01 # timestep
    softening    = 0.01 # softening length
    G            = 1.0  # Newtons Gravitational Constant
    plotRealTime = True # plotting as the simulation goes along
    
    np.random.seed(42)
    
    mass = 20.0*np.ones((N, 1))/N # total mass of particles is 20
    pos  = np.random.randn(N, 3)
    vel  = np.random.randn(N, 3)
    
    # Convert to Center of Mass frame
    vel -= np.mean(mass*vel, 0) / np.mean(mass)
    
    # Calculate init gravitational accelerations
    acc = acceleration(pos, mass, G, softening)
    
    # Calculate initial energy of system
    KE, PE = energy(pos, vel, mass, G)
    
    # Number of timesteps
    Nt = int(np.ceil(tEnd/dt))
    
    # Save energies, particles orbits for plotting trails
    pos_save = np.zeros((N, 3, Nt+1))
    pos_save[:, :, 0] = pos
    KE_save = np.zeros(Nt+1)
    KE_save[0] = KE
    PE_save = np.zeros(Nt+1)
    PE_save[0] = PE
    t_all = np.arange(Nt+1)*dt
    
    # pre figure
    fig = plt.figure(figsize=(4, 5), dpi=80)
    grid = plt.GridSpec(3, 1, wspace=0.0, hspace=0.3)
    ax1 = plt.subplot(grid[0:2,0])
    ax2 = plt.subplot(grid[2, 0])
    
    #simulation Main loop
    for i in range(Nt):
        vel += acc*dt/2.0
        
        pos += vel*dt
        
        acc = acceleration(pos, mass, G, softening)
        
        vel += acc*dt/2.0
        t += dt
        
        KE, PE = energy(pos, vel, mass, G)
        # Save energies
        pos_save[:, :, i+1] = pos
        KE_save[i+1] = KE
        PE_save[i+1] = PE
        
        # Plot in real time
        if plotRealTime or (i == Nt -1):
            plt.sca(ax1)
            plt.cla()
            xx = pos_save[:,0,max(i-50,0):i+1]
            yy = pos_save[:,1,max(i-50,0):i+1]
            plt.scatter(xx,yy,s=1,color=[.7,.7,1])
            plt.scatter(pos[:,0],pos[:,1],s=10,color='blue')
            ax1.set(xlim=(-2, 2), ylim=(-2, 2))
            ax1.set_aspect('equal', 'box')
            ax1.set_xticks([-2,-1,0,1,2])
            ax1.set_yticks([-2,-1,0,1,2])

            plt.sca(ax2)
            plt.cla()
            plt.scatter(t_all,KE_save,color='red',s=1,label='KE' if i == Nt-1 else "")
            plt.scatter(t_all,PE_save,color='blue',s=1,label='PE' if i == Nt-1 else "")
            plt.scatter(t_all,KE_save+PE_save,color='black',s=1,label='Etot' if i == Nt-1 else "")
            ax2.set(xlim=(0, tEnd), ylim=(-300, 300))
            ax2.set_aspect(0.007)

            plt.pause(0.001)
    
    plt.sca(ax2)
    plt.xlabel('time')
    plt.ylabel('Energy')
    ax2.legend(loc='nbody.png', dpi=240)
    
    return 0
    
if __name__=="__main__":
    main()