# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:36:39 2020

@author: Pratiksha
"""
import math
def countBits(n): 
    return int((math.log(n) / math.log(2)) + 1)
  
def flipBits(n):
    n1 = countBits(n)
    val=''
    val=val+n1*'1'
    val=(int(val,2))
    return val-n

i=int(input("Enter the number : "))
print('Value after flipping : ',flipBits(i))