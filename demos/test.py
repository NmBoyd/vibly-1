from slippy.slip import *
import numpy as np
import matplotlib.pyplot as plt

p = {'mass':80.0, 'stiffness':8200.0, 'resting_length':1.0, 'gravity':9.81,
    'angle_of_attack':1/5*np.pi}
x0 = np.array([0, # x position
    0.85, # y position
    5.5, # x velocity
    0, # y velocity
    0, # foot position x
    0]) # foot position y
x0 = reset_leg(x0, p)
p['total_energy'] = compute_total_energy(x0, p)
sol = step(x0, p)

plt.plot(sol.y[0], sol.y[1], color='orange')
plt.show()