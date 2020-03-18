# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:25:52 2020

@author: Pratiksha
"""

def countSetBits(n): 
    count = 0
    while (n): 
        n &= (n-1)  
        count+= 1    
    return count 

i = int(input("Enter the number : "))
if(countSetBits(i)==1 and i!=1):
    print(True)
else:
    print(False)
