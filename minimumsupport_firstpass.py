# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:59:32 2017

@author: Keerthi
"""

def first_pass(seq_k,singleton,min_support):
    # singleton array with minimum support by all candidates
    min_support_fpass = []
    '''
    for j in xrange(len(singleton)):
        min_support_fpass[j] = [j]
    '''
    for j in xrange(len(singleton)):
        counter = 0
        for k in xrange(len(seq_k)):
            dum_arr = cseq[k][1:]
            dum_size = len(dum_arr)
            #flag = 0
            for l in xrange(dum_size):
                if singleton[j] in  dum_arr[l]:
                    counter = counter + 1
                    break
        if counter >= min_support:
            min_support_fpass.append([singleton[j],counter])
         
    
    
    return min_support_fpass
