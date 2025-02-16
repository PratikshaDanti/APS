# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:21:38 2020

@author: Pratiksha

To find the maximum contiguous subarray and print its starting and end index 
"""

from sys import maxsize 
def maxSubArraySum(a,size): 
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range(0,size): 
        max_ending_here += a[i] 
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
    print ("Maximum contiguous sum is %d"%(max_so_far)) 
    print ("Starting Index %d"%(start)) 
    print ("Ending Index %d"%(end)) 
  
a = list(map(int,input('Enter the values : ').split()))
maxSubArraySum(a,len(a)) 
