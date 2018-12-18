# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:10:47 2018

@author: ahall
"""
from datetime import datetime
import re

with open("day4.txt","r") as infile:
    input_text = infile.readlines()

processed_list = list()
for line in input_text:
    processed_list.append(line.rstrip())
    
dct = {}
for line in processed_list:
    line=line.replace('[','')
    entry=line.split('] ')
    dct[datetime.strptime(entry[0],'%Y-%m-%d %H:%M')]=entry[1]