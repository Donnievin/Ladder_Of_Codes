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

#Now center the galaxy
Middle_of_galaxy = pynbody.analysis.halo.center(s)
#print(Middle_of_galaxy)


#This is the function that found the black hole
def findBH(s):
    BH = s.stars[pynbody.filt.LowPass('tform', 0.0)]
    return BH
Found_one= findBH(s)

#This will print the position of the black hole
#print(Found_one['pos'])
#position = [[-634.00464133 1258.07020815   29.86851614]]



#Next step: Vel of BH




#Find the velocity of the black hole itself
BH_Vel = (Found_one['vel'])
x = np.array([vel[0] for vel in BH_Vel])
y = np.array([vel[1] for vel in BH_Vel])
z = np.array([vel[2] for vel in BH_Vel])
vel_answer = np.sqrt((x)**2 + (y)**2 + (z)**2)
#print(vel_answer)
#print(s['vel'].units)




#Next step: Vel of Galaxy




#Now we find the velocity of the entire galaxy and print the units
Galaxy_Vel = (s['vel'])
#print(Galaxy_Vel)

#turn x,y,z components into their own array
Gal_x = np.array([vel[0] for vel in Galaxy_Vel])
Gal_y = np.array([vel[1] for vel in Galaxy_Vel])
Gal_z = np.array([vel[2] for vel in Galaxy_Vel])

#How many num are in each array
number_x = len(Gal_x)
number_y = len(Gal_y)
number_z = len(Gal_z)

#Sum up each array
vx = Gal_x.sum()
vy = Gal_y.sum()
vz = Gal_z.sum()

#Take the sum and divide it by how many nums we added together
velocity_x = vx / number_x
velocity_y = vy / number_y
velocity_z = vz / number_z




#Next step: Subtracting components from one another

Resultant_x = velocity_x - x
Resultant_y = velocity_y - y
Resultant_z = velocity_z - z

Answer = np.sqrt((Resultant_x)**2 + (Resultant_y)**2 + (Resultant_z)**2)
print(Answer)

