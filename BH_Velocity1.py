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

#This is the function that found the black hole
def findBH(s):
    BH = s.stars[pynbody.filt.LowPass('tform', 0.0)]
    return BH
BH= findBH(s)



#First step: Positioning the blackhole


#Need this pynbody faceon to tell how far the BH is from the center
pynbody.analysis.angmom.faceon(s)
BH_pos = BH['pos']
BHx = BH_pos[:,0]
BHy = BH_pos[:,1]
BHz = BH_pos[:,2]
BH_answer = np.sqrt((BHx)**2 + (BHy)**2 + (BHz)**2)
#print(BH_answer)

