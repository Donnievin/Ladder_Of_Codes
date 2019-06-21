#import all the good stuff!
#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import pynbody
import pylab
import numpy as np
import matplotlib.pylab as plt
import astropy.units as u

#Separate stars from everything (Done)
#Find AVG velocity of stars

#Now I need a code that will load the simulation (s will stand for simulation)
s = pynbody.load("cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096.5.std")

#The following code will change the units to make it more appealing
s.physical_units()

#I need a code to separate the stars from the rest of the stuff
#This code extracts the velocity of every star in the simul.
stars = s.stars['vel']

#This code gives me an exact number of how many stars there are
num_of_stars = s.stars[0:]
total_stars = len(num_of_stars)

velocity_i = np.array([vel[0] for vel in stars])
velocity_j= np.array([vel[1] for vel in stars])
velocity_k = np.array([vel[2] for vel in stars])
vel_total = np.array([velocity_i, velocity_j , velocity_k] )
#print(vel_total)

plt.hist(velocity_i, color = 'b', bins = 100)
plt.xlabel("x")
plt.ylabel("frequency")
plt.axvline(velocity_i.mean(), color='k', linestyle='dashed', linewidth=1)
plt.legend()
plt.show()


plt.hist(velocity_j, color = 'g', bins = 100)
plt.xlabel("y")
plt.ylabel("frequency")
plt.axvline(velocity_j.mean(), color='k', linestyle='dashed', linewidth=1)
plt.legend()
plt.show()

plt.hist(velocity_k, color = 'y', bins = 100)
plt.xlabel("z")
plt.ylabel("frequency")
plt.axvline(velocity_k.mean(), color='k', linestyle='dashed', linewidth=1)
plt.legend()
plt.show()
