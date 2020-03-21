# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:06:50 2020

@author: Pratiksha

This function analyses a list/string and helps to return the top n entities
in the list/string according to their number of occurences in descending order
where n is a number that is specified by the programmer.

"""

from collections import Counter 
  
arr =list(map(int,input('Enter the list : ').split())) 
top=int(input('Enter number of values required : '))
counter = Counter(arr) 
top_values = counter.most_common(top) 
print(top_values) 