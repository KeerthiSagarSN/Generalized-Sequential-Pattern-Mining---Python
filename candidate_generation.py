# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:42:21 2017

@author: Keerthi
"""

#from subseq_gen import subseq_rule 



def candidate_gen(k,seq_k):

    # New frequent list
    
    
    #k = 1
    
    from copy import deepcopy
    #seq_k_1 = deepcopy(seq_k)
     
    new_seq_k = [] # Intializing empty list
    # For k = 1 Frequent Sequence
    # Getting the size of previous frequent set- Either  1- seq, 2-seq or 3-seq frequent sets
    
    if k == 0: # Special rule for candidate generation
       new_seq_k = seq_k 
       new_seq_k_pruned = seq_k
    
    if k == 1: # Special case generate all possible 2 sequence candidate configurations
       
       for m in xrange(len(seq_k)):
           for n in xrange(m,len(seq_k),1):
               dum1 = [[seq_k[m]]+[seq_k[n]]]
               new_seq_k.append(dum1)
               dum = [[seq_k[m]],[seq_k[n]]] 
               new_seq_k.append(dum)
 
        
    if k > 1:
        for j in xrange(len(seq_k)): # Every combination possible - Every k sequence we need to compare with itemfrequent sets
            dum = [] # Dummy variable
            dum = deepcopy(seq_k[j])
            sub_f = dum[1:] # Getting the subsequent element: i.e only intermediate terms, excluding first and last term
            
            if len(dum[0]) > 1:
                dum_1 = []
                dum_1 = dum[0][1:]
                sub_f = [dum_1] + sub_f # Concatenate first element by popping out the first element
            
            for z in xrange(len(seq_k)):
                if j != z :
                    dum_l = [] # Dummy variable
                    dum_l = list(seq_k[z])
                    sub_l = dum_l[:-1] # Getting the subsequent element: i.e only intermediate terms, excluding first and last term
                    
                    if len(dum_l[-1]) > 1:
                        dum_l2 = []
                        dum_l2 = dum_l[-1][:-1] # Concatenate the last element by popping out the last element from the subsequence
                        sub_l = sub_l + [dum_l2]
                    if sub_f == sub_l: # Check if two candidate sub-sequence match according to the rule given in the paper
                        
                        if (len(dum_l[-1]) > 1): # If the last element in the second subsequence is greater than one element, just concacatenate that to the main subseq
                            new_seq_dum = []
                            new_seq_dum = dum[:-1]    
                            new_seq_dum.append(dum_l[-1])
                            new_seq_k.append(new_seq_dum)
                        else: # Else concatenate both first and second subseq
                            new_seq_dum = []
                            new_seq_dum = dum    
                            new_seq_dum.append(dum_l[-1])
                            new_seq_k.append(new_seq_dum)
    
    
    return new_seq_k                
            
            
def candidate_prune(new_seq_k,seq_k): # Candidate pruning
    new_seq_k_pruned = []
    from subsequence_gen import subseq_rule       
    for w in xrange(len(new_seq_k)):
        subseq1 = subseq_rule(new_seq_k[w])
        mincnt = 0
        for m in xrange(len(subseq1)):
            if subseq1[m] in seq_k:
                mincnt = mincnt + 1
            else:
                print ('Candidate pruned')
                break
            if mincnt == len(subseq1):
               new_seq_k_pruned.append(new_seq_k[w]) 
    return new_seq_k_pruned        
            
        
        
        
        