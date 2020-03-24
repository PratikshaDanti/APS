# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:32:15 2020

@author: Pratiksha
"""

t = int(input('Enter number of test cases : ').strip())
for a0 in range(t):
    n = int(input('Enter value of n : ').strip())
    sum_of_n=((n*(n+1))/2)**2
    sum_of_n_square=((n*(n+1)*(2*n+1))/6)
    print('Result is : ',int(sum_of_n-sum_of_n_square))
