#import all the good stuff!
#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import pynbody
import pylab
import numpy as np
import matplotlib.pylab as plt
import astropy.units as u

'''
Steps to creating  for loop
1. Create a file/array/list you want to cycle through
2. "For number (x) in [range]: if "
3. Tell it what you want it to do for all the x's in this file
4. print x
'''

#Now I need a code that will load the simulation (s will stand for simulation)
s = pynbody.load("cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096.5.std")

#The following code will change the units to make it more appealing
s.physical_units()
#This is a function to find the blackholes
def findBH(s):
    BH = s.stars[pynbody.filt.LowPass('tform', 0.0)]
    return BH
BH = findBH(s)


#Below is a for loop outline
'''
for num in range(5):
    print(num)
'''

'''
#Here is a for loop that will find each black hole in the entire simulation
#It will print their positions
for x in s:
    #Don't forget to center the galaxy with this
    pynbody.analysis.angmom.faceon(s)

    #printing the position by itself will give us an array of i,j,k
    #Instead use the function we made before
    BH_pos = BH['pos']
    BHx = BH_pos[:,0]
    BHy = BH_pos[:,1]
    BHz = BH_pos[:,2]
    BH_answer = np.sqrt((BHx)**2 + (BHy)**2 + (BHz)**2)
    print "I found the black hole and it is at:" , BH_answer
'''
    
for i in s:

    #Here I will make a another loop which will solve for vel around BH
    radius = 0.5 #KPC
    sphere= pynbody.filt.Sphere(radius, cen= (-634.00464133,1258.07020815, 29.86851614))
    #This code tells us how many stars are in this section
    num_of_stars = s.stars[0:]
    in_sphere = num_of_stars[sphere]
    #This is how many stars there are
    total_stars = len(in_sphere)
    #This find their velocity
    velocity = in_sphere['vel']
    #Now we need to find the velocity of these stars in x,y,z
    x = np.array([vel[0] for vel in velocity])
    y = np.array([vel[1] for vel in velocity])
    z = np.array([vel[2] for vel in velocity])
    #Now we can find the average of these by dividing by the total
    vel_answer = np.sqrt((x)**2 + (y)**2 + (z)**2)

    #Now divide by total number of stars
    velocity = vel_answer.sum() / total_stars
    answer = velocity
    print 'The stars around the black hole are moving at:', answer

'''
    
    BH_vel = BH[
    print(['vel'])
    print(I found youre blackhole)
'''
    
