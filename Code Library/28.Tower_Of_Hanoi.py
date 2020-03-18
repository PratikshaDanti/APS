# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 07:13:47 2020

@author: Pratiksha
"""

def TowerOfHanoi(n,x,y,z):
    if n>=1:
        TowerOfHanoi(n-1,x,z,y)
        print('move top of the disk from tower : ',x,' to top of the tower : ',y)
        TowerOfHanoi(n-1,z,y,x)

n=int(input('Enter the number of disks : '))
TowerOfHanoi(n,'A','C','B')