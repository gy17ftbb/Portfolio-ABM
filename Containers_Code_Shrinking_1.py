#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:19:57 2019

@author: fatintasnimbaharuddin
"""
#from Prac1, copy the module and coordinate generator
import operator
import random 
import matplotlib.pyplot as plot
#import numpy as np
#First trial before getting rid of x0 & y0 
#y0 = random.randint(0,99)
#x0 = random.randint(0,99)
#agents = []
#agents.append([y0,x0])
# print (y0, x0) - checking (OK)


# getting rid of y0 and x0

#container for agent_ and assignment of random coordinate 
agent_ = [] 
agent_.append ([random.randint(0,99),random.randint(0,99)])
agent_.append ([random.randint(0,99),random.randint(0,99)])

print ("Agents Coordinate:", agent_) #using function max(), to know which of the agent is further east (larger x) in y,x coordinate. 
print("Furthest East Agent's Coordinate:", max(agent_, key=operator.itemgetter(1))) 
#max is function (key is name, operator.itemgetter is the package under operator module)
#external library to plot data in graphs to plot the agents location 

plot.ylim(0,99)
plot.xlim(0,99)
plot.scatter(agent_[0][1],agent_ [0][0])
plot.scatter(agent_[1][1],agent_ [1][0])
max_east = max(agent_, key=operator.itemgetter(1)) #getting the furthest east value from X axis
plot.scatter(max_east[1],max_east[0], color='red') #plotting (x, y, colour)
plot.show()