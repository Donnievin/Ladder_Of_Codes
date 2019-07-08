#import all the good stuff!
#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import pynbody
import numpy as np
import readcol

'''
Steps to creating  for loop
1. Create a file/array/list you want to cycle through
2. "For number (x) in [range]: if "
3. Tell it what you want it to do for all the x's in this file
4. print x
'''

#Now I need a code that will load the snapshots(s will stand for simulation)
#s = pynbody.load("cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096.5.std")
#"/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/"

files = readcol.readcol('/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/files.list')
all_files = files[0:]

#This is a function to find the blackholes
def findBH("all_files"):
    BH = all_files[pynbody.filt.LowPass('tform', 0.0)]
    return BH
BH = findBH("all_files")
print(BH)
'''
#We used this function to calculate the velocity of the stars

#Here I will make a another loop which will solve for vel around BH
radius = 0.5 #KPC
sphere= pynbody.filt.Sphere(radius, cen= (-634.00464133,1258.07020815, 29.86851614))
#This code tells us how many stars are in this section
num_of_stars = all_files.stars[0:]
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


#Below is a for loop outline
'''
for num in range(5):
    print(num)
'''
for i in all_files :
    #Center it
    pynbody.analysis.angmom.faceon(all_files)
    stars_vel = velocity[i]
    print 'The stars around the black hole are moving at:', stars_vel
'''
