#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 10:14:10 2020
using selenium to open a page and search for a tracking number

@author: nick
"""

from selenium import webdriver

#set the browser to firefox
browser = webdriver.Firefox()

#goto google.com
browser.get('https://www.google.com')

#find the search bar element
googleSearchBar = browser.find_element_by_name("q")

googleSearchBar.send_keys("Taylor Kicksey Maryville Missouri")
googleSearchBar.submit()