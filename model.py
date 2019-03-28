#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 23:13:23 2019

@author: fatintasnimbaharuddin
"""

# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.
# import random - importing module 
import random 
#movement for y0 and x0
y0 = 50
x0 = 50 
#print (y0, x0) - checking (OK). Assign variable to use the module
random_number_y0 = random.random()
#print (random_number) - checking (OK)
#assign if else to the random_number variable using random.random 
if  random_number_y0 < 0.5:
    y0 = y0 + 1 #can also be written as y0 += 1 
else:
    y0 = y0 - 1 #can also be written as y0 -= 1


#assingning code to move x0
random_number_x0 = random.random()
if random_number_x0 < 0.5:
    x0 = x0 + 1 #can also be written as x0 += 1
else:
    x0 = x0 - 1 #can also be written as x0 -= 1 
print (y0, x0)

#solution to have independence move for y0 and x0 as the random.random assignment were made for each. 


#movement for y1 and x1- the second agent
y1 = 50
x1 = 50 
#print (y1, x1) - checking (OK). Assign variable to use the module
random_number_y1 = random.random()
#print (random_number) - checking (OK)
#assign if else to the random_number variable using random.random 
if  random_number_y1 < 0.5:
    y1 = y1 + 1 #can also be written as y1 += 1 
else:
    y1 = y1 - 1 #can also be written as y1 -= 1


#assingning code to move x1
random_number_x1 = random.random()
if random_number_x1 < 0.5:
    x1 = x1 + 1 #can also be written as x1 += 1
else:
    x1 = x1 - 1 #can also be written as x1 -= 1 
print (y1, x1)

#solution to have independence move for y1 and x1 as the random.random assignment were made for each. 
#distance calculation using pytjagorean theorem with y^2 + x^2 = hyp^2.

y = y1 - y0 
x = x1 - x0 
hyp = ((y)**2 + (x)**2)** 0.5
print (y, x, hyp)

# Randomise starting points within a 100x100 grid, with the coordinates being integer values between and including 0 and 99.  
# start coordinate for Agent 0
st_y0 = random.randint (0, 99)
st_x0 = random.randint (0, 99)
print ("Coordinate Agent 0: ", st_y0, st_x0) 

# start coordinate for Agent 1 
st_y1 = random.randint (0, 99)
st_x1 = random.randint (0, 99)
print ("Coordinate Agent 1: ",st_y1, st_x1) 

# calculate distance between both agents
dis_y = st_y0 - st_y1 
dis_x = st_x0 - st_x1 
hypo = ((dis_y)**2 + (dis_x)**2)** 0.5
print ("Y distance:", dis_y, "X distance:", dis_x, "Distance:", hypo)

        


