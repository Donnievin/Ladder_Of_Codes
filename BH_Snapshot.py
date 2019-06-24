#import all the good stuff!
#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import pynbody
import pylab
import pynbody.plot.sph as sph
import numpy as np
import matplotlib.pylab as plt
import astropy.units as u

#Now I need a code that will load the simulation (s will stand for simulation)
s = pynbody.load("cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096.5.std")

#The following code will change the units to make it more appealing
s.physical_units()

#This is the function that found the black hole
def findBH(s):
    BH = s.stars[pynbody.filt.LowPass('tform', 0.0)]
    return BH
here= findBH(s)

#This code creates a sphere around the black holes position
radius = 0.5
sphere = pynbody.filt.Sphere(radius, cen= (-634.00464133,1258.07020815, 29.86851614))
print(sphere)

#This code will sum all the stars into a variable
num_of_stars = s.stars[0:]
in_sphere = num_of_stars[sphere]


pynbody.analysis.angmom.faceon(in_sphere)
pynbody.plot.stars.render(s,width='0.25 kpc')
plt.show()
'''
properties = dir(sphere)
print(properties)


sphere = ['pos'][-634.00464133,1258.07020815, 29.86851614]
#Now that we have a sphere around the BH, we can print it's image of stars
pynbody.analysis.angmom.sideon(sphere)
pynbody.plot.stars.render(s,width= '0.5 kpc')

plt.show()
'''
