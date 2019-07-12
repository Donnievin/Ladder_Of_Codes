#import all the good stuff!
#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import pynbody
import pylab
import pynbody.plot.sph as sph
import numpy as np
import matplotlib.pylab as plt
from pynbody.analysis import profile

#Now I need a code that will load the simulation (s will stand for simulation)
s = pynbody.load("cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096.5.std")


#The following code will change the units to make it more appealing
s.physical_units()

#This finds the blackhole
def findBH(s):
    BH = s.stars[pynbody.filt.LowPass('tform', 0.0)]
    return BH


#Center it
pynbody.analysis.angmom.faceon(s)


#I need to start by defining each profile (defaulted on xy plane)
p = pynbody.analysis.profile.Profile(s,min='.1 kpc', max='2 kpc', type = 'log')
pgas = pynbody.analysis.profile.Profile(s.g,min='.1 kpc', max='2 kpc', type = 'log')
pdm = pynbody.analysis.profile.Profile(s.d,min='.1 kpc', max='2 kpc', type = 'log')
pstars = pynbody.analysis.profile.Profile(s.s,min='.1 kpc', max='50 kpc', type = 'log')

'''
#This code tells me what keys I can call on to plot
print(p.derivable_keys())
'''


#Let's start making the plot by assigning subplots
f, axs = plt.subplots(1,4,figsize=(10,5))

#Making the profiles
axs[0].plot(pstars['rbins'],pstars['density'], 'k', color = 'b')
axs[0].semilogx()
axs[0].semilogy()
axs[0].set_xlabel('Radius [kpc]')
axs[0].set_ylabel(r'$\Sigma_{\star}$ [M$_{\odot}$ kpc$^{-3}$]')
axs[0].set_title('Stars')


axs[1].plot(pgas['rbins'],pgas['density'], 'k', color = 'r')
axs[1].semilogx()
axs[1].semilogy()
axs[1].set_xlabel('Radius [kpc]')
axs[1].set_ylabel(r'$\Sigma_{\star}$ [M$_{\odot}$ kpc$^{-3}$]')
axs[1].set_title('Gas')

axs[2].plot(pdm['rbins'],pdm['density'], 'k', color = 'g')
axs[2].semilogx()
axs[2].semilogy()
axs[2].set_xlabel('Radius [kpc]')
axs[2].set_ylabel(r'$\Sigma_{\star}$ [M$_{\odot}$ kpc$^{-3}$]')
axs[2].set_title('Dark Matter')

axs[3].plot(p['rbins'],p['density'], 'k')
axs[3].semilogx()
axs[3].semilogy()
axs[3].set_xlabel('Radius [kpc]')
axs[3].set_ylabel(r'$\Sigma_{\star}$ [M$_{\odot}$ kpc$^{-3}$]')
axs[3].set_title('ALL')
plt.show()
