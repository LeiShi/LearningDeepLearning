# -*- coding: utf-8 -*-
"""
number deletion problem

Question: given the n number cycle [0, 1, 2, ..., n-1], if we delete every 
third number from start, continue doing it from beginning when reaches the end,
what is the last number got deleted?

Rough idea: linked list with next and previous number stored. Actually 
carrying out the deletion process.

Created on Sun Sep 10 23:16:33 2017

@author: shile
"""

import numpy as np
from timeit import timeit

def deletion(n):
    
    next_list = np.arange(n) + 1
    next_list[-1] = 0

    # counter for remaining numbers
    remain = n
    # record of the most recent deleted number
    deleted = -1
    # current number 
    current = 0
    # keep doing the deletion until total number reduces to 2
    while(remain > 2):
        current = next_list[current]
        deleted = next_list[current]
        next_list[current] = next_list[deleted]
        current = next_list[current]
        remain = remain-1
        
    return deleted
    
# test script
if __name__ == "__main__":
    #print "TEST "
    deletion(5)
    #for n in np.power(10,np.arange(2)):
    for n in np.power(2,np.arange(5)):
        print "n: {0}".format(n)
        print "deleted: {0}".format(deletion(n))
    
    

