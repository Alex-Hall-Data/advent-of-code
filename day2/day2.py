# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 12:28:52 2018

@author: ahall
"""

import itertools

input_text = open("day2_input.txt","r").readlines()

processed_list = list()
for line in input_text:
    processed_list.append(line.rstrip())
    
twos_list = list()
threes_list = list()

for line in processed_list:
    twos = 0
    threes = 0
    for letter in set(line):
        if line.count(letter)==3:
            threes=threes+1
            
        elif line.count(letter)==2:
            twos = twos+1
            
    twos_list.append(twos)
    threes_list.append(threes)
  
twos_count=0
threes_count=0

for value in twos_list:
    if value >0:
        twos_count = twos_count+1
        
for value in threes_list:
    if value >0:
        threes_count=threes_count+1
        
print(twos_count * threes_count)
    

###part 2
#compare list elements with one letter removed

for i in range(len(processed_list[0])):
    one_drop_list=list()
    for line in processed_list:
        one_drop_list.append(line[:i]+line[i+1:])
    for line in one_drop_list:
        if one_drop_list.count(line)>1:
            print(line)
            print(i)
            break
