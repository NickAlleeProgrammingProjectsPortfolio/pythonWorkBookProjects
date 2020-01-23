#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 19:44:11 2020

@author: nick

this will email myself.
its simply a test
"""
import ezgmail
try:
    ezgmail.send("nickallee8529@gmail.com","this was sent from python code", "the body of this message is pretty amazing")
    print("email sent")
except:
    print("failed")
