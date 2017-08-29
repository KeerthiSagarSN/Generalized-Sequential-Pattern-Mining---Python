# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 13:55:56 2017

@author: Keerthi
"""
# def subseq_gen(newsubseq):
#    subseq.append(dum)

def subseq_rule(seq): # Import the subsequence
    subseq = []
    # Rule 1 - subsequence is derived by removing the first element from the sequence
    if len(seq[0]) == 1:
        dum = [] # Dummy variable
        dum = list(seq[1:])
        subseq.append(dum)
    # Rule 2 - subsequence is derived by removing the last element of the sequence
    if len(seq[-1]) == 1:
        dum = list(seq[0:-1])
        subseq.append(dum)
    # Rule 3 - subsequence c is derived from seq "s" by dropping an item from an element si which has at least 2 items
    for k in xrange(len(seq)):
        if len(seq[k]) > 1:
            dum = []
            seq_new = list(seq)
            dum = list(seq[k])
            for j in xrange(len(dum)):
                dum1 = []
                dum1 = list(dum)
                del dum1[j]
                seq_new[k] = list(dum1)
                seq_new1 = list(seq_new)
                subseq.append(seq_new1)
    return subseq                
                
            
    