# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:57:09 2017

@author: Keerthi
"""
# Find all the singleton elements
def singleton_gen(seq_k):
    # singleton array
    # Append all sequence to one list
    
    singleton_arr = []
    for j in xrange(len(seq_k)):
        dum_seq = seq_k[j][3:] # Generate a dummy sequence - of dimension 1
        arr_size = len(dum_seq) # Get the size of the tuple
        for k in xrange(arr_size):
            dum_size = len(dum_seq)
            for l in xrange(dum_size):
                dum = dum_seq[l]
                if dum in singleton_arr:
                    singleton_arr = singleton_arr
                else:
                    singleton_arr = singleton_arr + [dum]
    return singleton_arr

    
            
    