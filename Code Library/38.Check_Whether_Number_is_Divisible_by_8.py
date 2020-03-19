# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:29:45 2020

@author: Pratiksha
"""

n=int(input("Enter the number : "))
res = n
res = (res>>3)<<3
if res==n:
    print("Divisible by 8")
else:
    print("Not divisible by 8")