# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:36:28 2020

@author: Pratiksha
"""

def josephus(n, k):   
      if (n == 1): 
          return 1
      else: 
          return (josephus(n - 1, k) + k-1) % n + 1
      
n,k=map(int,input('Enter n and k values : ').split())
p=josephus(n,k)
print(p)