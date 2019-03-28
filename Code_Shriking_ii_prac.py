#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:23:40 2019

@author: fatintasnimbaharuddin
"""
import time
start = time.perf_counter() # The code to run, here.
import random 
import matplotlib.pyplot as plot 

def dist_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

num_of_agents = 10 
num_of_iterations = 100
agent_ = [] 

#create agents 
for i in range (num_of_agents):
    agent_.append([random.randint(0,99),random.randint(0,99)])
  
 #move agents    
for j in range (num_of_iterations):
    for i in range (num_of_agents):
      
        #for y
        if  random.random() < 0.5:
            agent_[i][0]= (agent_[i][0] + 1) % 100 
        else:
            agent_[i][0]= (agent_[i][0] - 1) % 100
        
        #for x
        if  random.random() < 0.5:
            agent_[i][1]= (agent_[i][1] + 1) % 100 
        else:
            agent_[i][1]= (agent_[i][1] - 1) % 100
     
#assigning plots limit 
    plot.ylim(0, 99)
    plot.xlim(0, 99)
    
    # Check if off edge and adjust.
    if agent_[i][0] < 0: #y
        agent_[i][0] = 0 
    if agent_[i][1] < 0: #x
        agent_[i][0] = 0 
    if agent_[i][0] > 99: #y
        agent_[i][0] = 99
    if agent_[i][1] > 99: #x
        agent_[i][0] = 99
        
#plot all agents
for i in range(num_of_agents): 
    plot.scatter(agent_[i][1],agent_[i][0])         
plot.show()

#calculate distance 
for agents_row_a in agent_:
    for agents_row_b in agent_:
        distance = dist_between(agents_row_a, agents_row_b)
        #print (distance) ok 
i= i + 1 
 
#end of timer 
end = time.perf_counter()
print("time = " + str(end - start))



    
    