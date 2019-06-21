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

#This group of code calls creates a variable for each column of data
i = np.array([vel[0] for vel in stars]).sum()
j= np.array([vel[1] for vel in stars]).sum()
k = np.array([vel[2] for vel in stars]).sum()

vel_answer = np.sqrt((i)**2 + (j)**2 + (k)**2)
print(vel_answer)
