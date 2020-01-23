#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:13:59 2020

create new folder and create an excel file in it.
add my the argument to the excel file

@author: nick
"""

import os, openpyxl
p = os.getcwd()
try:
    os.mkdir("excelFileFolder")
except:
    print("folder already exists")
os.chdir(p + "/excelFileFolder")
newBook = openpyxl.Workbook()
sheet = newBook["Sheet"]
sheet['A1'] = "i added this from python" 

newBook.save(filename = "pythonExcelFile.xlsx")
print("new folder and excel file made")