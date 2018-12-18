# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:27:22 2018

@author: ahall
"""
import re
import numpy as np

input_text = open("day3.txt","r").readlines()

processed_list = list()
for line in input_text:
    processed_list.append(line.rstrip())
    
regexed_list = list()
for i in range(len(processed_list)):
    processed_list[i] = re.sub(r'.*@', '', processed_list[i])
    processed_list[i] = re.sub('x',',',processed_list[i])
    processed_list[i] = re.sub(':',',',processed_list[i])
    processed_list[i] = processed_list[i].split(",")
    processed_list[i] =list(map(int,processed_list[i]))
    
maxdim= max([val for sublist in processed_list for val in sublist])
maxx = max([val for sublist in processed_list for val in sublist[2:3]])

maxdim=maxdim+maxx

area_matrix=np.zeros((maxdim,maxdim))

for line in processed_list:
    x=line[0]
    y=line[1]
    xdim=line[2]
    ydim=line[3]
    for xrange in range(xdim):
        for yrange in range(ydim):
            area_matrix[x+xrange , y+yrange] = area_matrix[x+xrange , y+yrange] + 1
            
np.sum(np.greater(area_matrix,1))

#part 2
#####
for i in range(len(processed_list)):
    line=processed_list[i]
    x=line[0]
    y=line[1]
    xdim=line[2]
    ydim=line[3]
    area_sum = np.sum(area_matrix[x:x+xdim,y:y+ydim])
    if(area_sum == xdim*ydim):
        print(i+1)
        break
    

