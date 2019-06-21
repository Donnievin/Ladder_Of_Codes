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

'''
The velocity of each star is in an i,j,k notation in each of their respective
lines and that is why I can not just use a ".sum()" on the whole variable that
I assigned to stars.

Instead, I had to sum it up in each individual direction by using a ".sum()" and then find
then find the average velocity in each direction
'''

#These codes sum up the velocity in each direction
velocity_i = np.array([vel[0] for vel in stars]).sum()
velocity_j= np.array([vel[1] for vel in stars]).sum()
velocity_k = np.array([vel[2] for vel in stars]).sum()

#Now I can take the avg in each direction
avg_in_x = velocity_i / total_stars
avg_in_y = velocity_j / total_stars
avg_in_z = velocity_k / total_stars


'''
#Then I can print these values to the screen
print(avg_in_x)
print(avg_in_y)
print(avg_in_z)
'''

#I need a vector addition for these three values of avg_velocity, however
#since all of their velocities are in their own respective direction,
#the vector sum will be an array of these values

avg_vel_total = np.array([avg_in_x, avg_in_y, avg_in_z] )
print(avg_vel_total)
print(s['vel'].units)

vel_answer = np.sqrt((avg_in_x)**2 + (avg_in_y)**2 + (avg_in_z)**2)
print(vel_answer)


#tlpsy
#box1
#5, 10, 11
#galaxy is cpt marvel 5


'''
#Now I can play around w/ the simulation
#For example, I can print the mass by using this code below
#mass = s[0:]['mass'].sum().in_units('kg')
#Don't forget to print so we can see it
#print(mass)

#I can also print the position
#position = s[0:]['pos'].sum().in_units('m')
#print(position)

#Now I wanna print the velocity


#This code told me what units to use for velocity (hard asf to find)
#velocity_units = s['vel'].units
#print(velocity_units)

#velocity = s[0:]['vel'].sum().in_units('km s**-1')
#print(velocity)

#This code tells me what properties of the simulation I can call on
#keys = s.loadable_keys()
#print(keys)


#properties = s[0:].properties.keys()
#print(properties)

#This code will find the avg velocity
#velocity = s[0:]['average velocity'].sum().in_units('meters per second')
#print(velocity)

#a= pynbody.analysis.halo.center(s[0:])
#im = pynbody.plot.image(s[0:].d, width = '500 kpc', cmap=plt.cm.Greys, units = 'Msol kpc^-2')

#cpt = s.cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096.5.std()
#This code should create the simulation for me to print

#print(cpt)


#sim =pynbody.plot.image(h1.g, width=100, cmap='Blues')
'''




#What is a histogram
#make a histogram for x, y, z
