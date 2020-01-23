#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 18:37:35 2020

@author: nick

making multiple folders named from a list of strings
"""

import os

p = os.getcwd()
myList = ["nick","taylor","ian","aidan","hayden","travis"]

for i in myList:
    os.mkdir(i+"'sFolderForThings")
    
print(os.listdir())