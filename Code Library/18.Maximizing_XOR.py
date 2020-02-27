# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:57:44 2020

@author: Pratiksha
"""

def maximizingXor(l, r):
    maxv=0
    for i in range(l,r+1):
        for j in range(l,r+1):
            m=i^j
            if m>maxv:
                maxv=m

    return maxv

if __name__ == '__main__':
    l,r=map(int,input('enter the limit values : ').split())
    val=maximizingXor(l,r)
    print('Result : ',val)
