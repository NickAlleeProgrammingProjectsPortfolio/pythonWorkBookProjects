#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 16:31:55 2020
multiclipboard
@author: nick with the help of the python programming book called automate the boring stuff with python

usage: mcb <argument> <argument2>
argument 1 can be save, delete, or list
argument is the string you want to save or delete

"""
import sys, pyperclip, shelve

myShelf = shelve.open("cliboardshelf")
if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        myShelf[sys.argv[2]] = pyperclip.paste()
        print("string saved")
    if sys.argv[1].lower() == "delete":
        myShelf.pop(sys.argv[2])
        print("string deleted")
if len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        print("list of strings:\n***********************************\n")
        keyValueList = list(myShelf.keys())
        for i in keyValueList:
            print(i)
        

myShelf.close()
