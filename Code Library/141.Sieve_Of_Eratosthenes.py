# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:00:48 2020

@author: Pratiksha
"""

def SieveOfEratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    for p in range(2, n): 
        if prime[p]: 
            print (p) 
  
if __name__=='__main__': 
    n = 30
    SieveOfEratosthenes(n) 
