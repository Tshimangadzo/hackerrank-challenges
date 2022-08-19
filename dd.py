#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.

def capitalize(s):
    list_ = [];
    for letters in s:
        list_.append(letters)
    
    if list_[0].islower():
        list_[0] = list_[0].upper()
    return "".join(list_)

def solve(s):
    list_ = s.split(" ")
    new_s = ''
    for values in list_:
        new_s =new_s+" "+capitalize(values)
    new_s = new_s.split(" ")
    del new_s[0]
    return " ".join(new_s)


solve("")