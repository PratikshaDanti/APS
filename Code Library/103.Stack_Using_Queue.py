# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:22:28 2020

@author: Pratiksha
"""

from queue import LifoQueue 
stack = LifoQueue(maxsize = 3) 
print(stack.qsize()) 
stack.put('a') 
stack.put('b') 
stack.put('c') 
  
print("Full: ", stack.full())  
print("Size: ", stack.qsize())  
  
print('\nElements poped from the stack') 
print(stack.get()) 
print(stack.get()) 
print(stack.get()) 
  
print("\nEmpty: ", stack.empty()) 
