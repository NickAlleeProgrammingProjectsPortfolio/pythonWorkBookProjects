#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:26:52 2020

This file will get a websites html and print it out
@author: nick
"""

import requests

res = requests.get('https://www.google.com/search?sxsrf=ACYBGNRr95DcRmc9RCOllHVb9GAl1VLN-g%3A1579393855729&ei=P6MjXsCZLO-MtgXs7Z7oBA&q=usps+tracking&oq=usps+tracking&gs_l=psy-ab.3..35i39j0l9.4743.4743..5679...0.2..0.134.134.0j1......0....1..gws-wiz.......0i71.KG7XoeDeqOA&ved=0ahUKEwiAtezNtI7nAhVvhq0KHey2B00Q4dUDCAs&uact=5')
try:
    res.raise_for_status()
except Exception as exception:
    print("there was an issue connection to the given website. Error: "+ exception)
print(res.text)
savedHtmlFile = open('savedHtmlFile.txt','wb')
for chunck in res.iter_content(1000000):
    savedHtmlFile.write(chunck)
savedHtmlFile.close()