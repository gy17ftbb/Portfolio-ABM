#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 23:13:23 2019

@author: fatintasnimbaharuddin
"""


import matplotlib.pyplot as plot
import agentframework
import csv
import random


environment = []

#reading csv  
f = open('in.txt', 'r', newline = '') 
csvReader = csv.reader(f, )


for row in csvReader:   #~loop through with for to get y,x value 
   rowlist=[]
   for value in row: #for word in parsed_line:
        rowlist.append(float(value))#data_line.append(float(word))
   environment.append(rowlist)
'''plot.imshow(environment)
plot.show() '''
f.close()

def distance_between(agent_row_a, agent_row_b):
    return (((agent_row_a.x - agent_row_b.x)**2) + 
        ((agent_row_a.y - agent_row_b.y)**2))**0.5

agent_ = []
num_of_agent = 100
num_of_iterations = 1000
neighbourhood = 20 
store= 0

#fig = matplotlib.pyplot.figure(figuresize=(7,7))
#ax= fig.add_axes[(0,0,1,1)]

# Make the agents.
for i in range(num_of_agent):
    agent_.append(agentframework.Agent(environment,store, agent_))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agent):
        random.shuffle(agent_)
        agent_[i].move()
        agent_[i].eat()
        agent_[i].share_with_neighbours(neighbourhood)
        

plot.xlim(0, 99)
plot.ylim(0, 99)
plot.imshow(environment)
for i in range(num_of_agent):
    plot.scatter(agent_[i].x, agent_[i].y)
plot.show()
