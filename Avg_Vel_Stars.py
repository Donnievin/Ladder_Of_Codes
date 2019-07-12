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
star_mass = s.stars['mass']

#This group of code calls creates a variable for each column of data
i = np.array([vel[0] for vel in stars])
j= np.array([vel[1] for vel in stars])
k = np.array([vel[2] for vel in stars])

#Now we solve for the magnitude of each
vel_mag = np.sqrt((i)**2 + (j)**2 + (k)**2)
print(vel_mag)

#Multiply by it's respective mass and add it together
Mag_Mass = (vel_mag * star_mass).sum()
Total_Mass = star_mass.sum()

#Divide the combined magnitude by the combined mass
Answer = Mas_Mass / Total_Mass
print(Answer)
