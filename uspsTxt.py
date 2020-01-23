#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:15:11 2020

@author: nick

input1: usps tracking number
input2: phone number

This will goto usps website and track the given package. then have the site send texts to the given phone number reguarding the package.
"""
import sys
from selenium import webdriver

trackingNumber = sys.argv[1]
phoneNumber = sys.argv[2]

#set the browser to firefox
browser = webdriver.Firefox()

#goto google.com
browser.get('https://www.google.com')

#find the search bar element
googleSearchBar = browser.find_element_by_name("q")

googleSearchBar.send_keys("USPS tracking " + trackingNumber)
googleSearchBar.submit()

trackButton = browser.find_element_by_css_selector('div.JC99Dd BmP5tf')
trackButton.click()
# =============================================================================
# 
# 
# trackButton = browser.find_element_by_css_selector('g-raised-button.F0QMMd ROyXJc bbCbFe Gfzyee hide-focus-ring izG2qf DKlyaf Loxgyb')
# trackButton.click()
# =============================================================================
