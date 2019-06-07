import readcol 
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pynbody 
#First import all the good stuff!

File_from_Jill = readcol.readcol('times.list')#this is an array
RedshiftData = File_from_Jill[:,0]
#This code 'extracts' a column of data

TimeData = File_from_Jill[:,1]
#This code sets a variable for the next column in my chart                      
plt.plot(TimeData,RedshiftData)
plt.xlabel("Time" )
plt.ylabel("Redshift")
#These are just codes to put labels on it and makes the graph

plt.tick_params(axis="x", labelcolor="b")
#Honestly don't know what this code does, but it seems important

plt.legend()
plt.show()
#DON IS DONE
