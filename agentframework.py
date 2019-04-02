#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:50:26 2019

@author: fatintasnimbaharuddin
"""
import random 
import operator
import matplotlib.pyplot as plot



"""def distance_between(agent_row_a, agent_row_b):
    return (((agent_row_a[0] - agent_row_b[0])**2) + 
        ((agent_row_a[1] - agent_row_b[1])**2))**0.5 """

num_of_agent = 10
num_of_iterations = 100
agent_ = []


class Agent():
   
    def __init__(self, environment, store, agent_):
        self.y = random.randint (0,99) #set y
        self.x = random.randint (0,99) #sey x 
        self.environment = environment
        self.store = 0
        self.agent_ = agent_

    def get_x(self):
        return self.x 
    
    def get_y(self):
        return self.y
    
    def move(self):
        #y position 
        self.y = random.randint(0,99)
        if self.y < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
            
        #x position
        self. x = random.randint(0,99)
        if self.x < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100  
        
    
    def eat (self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    def share_with_neighbours(self,neighbourhood):
        for agent_ in self.agent_:
            dist = self.distance_between(agent_)
            if dist <= neighbourhood:
                sum = self.store + self.store
                ave = sum/ 2 
                self.store = ave 
                agent_.store = ave 
                #print ("sharing" + str (dist) + " " + str(ave))
    
    def distance_between(self, agent_):
        return (((self.x + agent_.x)**2) + ((self.y - agent_.y) **2))**0.5
    pass 
    