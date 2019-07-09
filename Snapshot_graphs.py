#import all the good stuff!
#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import pynbody
import numpy as np
import readcol

#Now I need a code that will load the snapshots(s will stand for )
Path = "/media/jillian//cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/"
files = readcol.readcol('/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/files.list')
all_files = files[:,0]

#Tell where BH is Function
def findBH(s):
    BH = s.stars[pynbody.filt.LowPass('tform', 0.0)]
    return BH

#Give BH pos variable




all_positions = []
all_velocity = []



for i in all_files:
    s = pynbody.load(Path + i)
    s.physical_units()
    BH = findBH(s)
    
    #Don't forget to center the galaxy with this
    pynbody.analysis.angmom.faceon(s)
   
    #printing the position by itself will give us an array of i,j,k
    #Instead use the function we made before
    BH_pos = BH['pos']
    BHx = BH_pos[:,0]
    BHy = BH_pos[:,1]
    BHz = BH_pos[:,2]
    BH_answer = np.sqrt((BHx)**2 + (BHy)**2 + (BHz)**2)
    print(BH_answer)
    all_positions.append(BH_answer)
    
    #Center it
    pynbody.analysis.angmom.faceon(s)
    #Here I will make a another loop which will solve for vel around BH
    radius = 0.5 #KPC
    len_three = np.array([BHx[0], BHy[0], BHz[0]])
    #print(len_three)
    sphere= pynbody.filt.Sphere(radius, cen= (len_three))
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
    all_velocity.append(velocity)

    print 'The stars around the black hole in this snapshot are moving at:', velocity
    
print(all_velocity)
print(all_positions)

snapshot_array = ( 1,2,10,20)


plt.plot(snapshot_array, all_velocity)
plt.xlabel("Which snapshot" )
plt.ylabel("It's velocity")
#These are just codes to put labels on it and makes the graph

plt.tick_params(axis="x", labelcolor="b")
#Honestly don't know what this code does, but it seems important

plt.legend()
plt.show()
