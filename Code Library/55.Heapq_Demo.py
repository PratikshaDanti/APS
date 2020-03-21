# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:15:50 2020

@author: Pratiksha

This function helps to return the top n smallest/largest elements 
in any lists and here again n is a number specified.
"""

import heapq 
  
a = list(map(int,input('Enter the list : ').split()))
n=int(input('Enter n value : ')) 
print(heapq.nlargest(n, a)) 
print(heapq.nsmallest(n, a)) 
