# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:14:06 2020

@author: Pratiksha
"""

x,y=map(int,input('Enter 2 values : ').split())
mini=(y^(x^y) & -(x<y))
maxi=(x^(x^y) & -(x<y))
print('Minimum value is : ',mini)
print('Maximum value is : ',maxi)