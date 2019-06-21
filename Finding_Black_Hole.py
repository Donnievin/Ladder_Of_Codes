#import all the good stuff!
#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import pynbody
import pylab
import numpy as np
import matplotlib.pylab as plt
import astropy.units as u

#Now I need a code that will load the simulation (s will stand for simulation)
s = pynbody.load("cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096.5.std")

#The following code will change the units to make it more appealing
s.physical_units()

'''
#This code tells me what properties of the simulation I can call on
keys = s.loadable_keys()
print(keys)
'''

'''
Previous Student used a function which tells the computer to filter through
the simulation to find anything with 'tform' (time formed) equal to an integer
lower than 0.

This makes sense since BH have a negative 'tform' and all negative integers
are less than 0
'''

def findBH(s):
    BH = s.stars[pynbody.filt.LowPass('tform', 0.0)]
    return BH

#Set the function equal to a variable and print the variable
Found_one= findBH(s)
print(Found_one)

#Set the position equal to a variable and print the variable
Here_it_is = Found_one['pos']
print(Here_it_is)

#To find the distance, we will need to separate each distance (i,j,k) into
#their own variable
x = np.array([pos[0] for pos in Here_it_is])
y = np.array([pos[1] for pos in Here_it_is])
z= np.array([pos[2] for pos in Here_it_is])

#Then we can use the formula for vectors
answer = np.sqrt((x)**2 + (y)**2 + (z)**2)
print(answer)

units = s['pos'].units
print(units)

data = [Found_one['mass'], Found_one['r']]
print(data)
