# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 05:43:32 2020

@author: Pratiksha
"""

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        print(k-1 if ((k-1) | k) <= n else k-2)
        
