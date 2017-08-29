# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 23:04:59 2017

@author: Keerthi
"""

# Main file - Run this for the GSP

### Input the database
from input_data import input_db # Import the database file and the process file
# Find the inputdb - Inputt d
#import inputdb # Database file - With all customer data,transaction data
### User specified input
min_support_input = input('Enter the minimum support confidence (integer value from 1 t0 100)')
window_size = 	input('Enter the window size (integer value from 0 t0 100)')
min_gap = input('Enter the minimum gap (integer value from 1 t0 n)')
max_gap = input('Enter the maximum gap (integer value from 1 t0 n, number greater than min_gap)')

while max_gap < min_gap:
    print('Minimum gap entered is' + str(min_gap))
    max_gap = input('Enter the maximum gap (integer value from 1 t0 n, number greater than min_gap)')
import os

inputdb = "inputdb.txt" # Place the database in the same folder as the main.py
  
# proc_db - Processesed database - Has integer assigned every item, 
#input_db - Input database - With actual data and a hash, 
#input_db_reverse - Reversed hash database with data and key(integer)
[proc_db,input_data,input_db_reverse,cust_size] = input_db(inputdb)
# proc_db - First column - 
### End the import of databasse

# Singleton generation - Not required, but yet all singleton are documented
from singleton import singleton_gen
singleton_arr = singleton_gen(proc_db)
### End singleton

# Getting the single element and its transaction time in an array
#from single_element import single_element_gen

# database sequence with time stamp of each customer
from database_sequence import database_seqfn,item_database
database_seq = database_seqfn(proc_db,cust_size)
20

# Get transaction times for each item for each customer: item_database_time
# Get if the item is present for a customer: item_database_cust

item_database_cust,item_database_time = item_database(database_seq,singleton_arr)
# Candidate generation - Maximal sequence possible
from candidate_generation import candidate_gen,candidate_prune

from support_count import support_count_gen
# Minimum support count
min_support = min_support_input*(cust_size)/100.0
min_support = int(min_support)
# Importing the function
#from support_count import support_count_gen
#for k in xrange(1,len(singleton_arr),1):
cand_seq = []
support_cand = [] # Support candidate
for k in xrange(0,3,1): # Counter from 1, not a pythonic way, start from 0.
    if k == 0: # Special case: First minimum count
        cand_seq.append(candidate_gen(k,singleton_arr))
        support_cand_dum = support_count_gen(cand_seq,database_seq,min_support,window_size,max_gap,min_gap,item_database_cust,item_database_time,k)
        support_cand.append(support_cand_dum)
    
        
    if k == 1: # Special case - Dont prune here
        cand_seq.append(candidate_gen(k,support_cand[k-1])) # Candidate generation
        support_cand_dum = support_count_gen(cand_seq,database_seq,min_support,window_size,max_gap,min_gap,item_database_cust,item_database_time,k)
        support_cand.append(support_cand_dum)
    if k > 1:
        cand_seq.append(candidate_gen(k,support_cand[k-1])) # Candidate generation
        cand_seq_prune = candidate_prune(cand_seq[k],cand_seq[k-1])
        support_cand_dum = support_count_gen(cand_seq_prune,database_seq,min_support,window_size,max_gap,min_gap,item_database_cust,item_database_time,k)
        support_cand.append(support_cand_dum)
    
    if len(support_cand[k]) == 0:
        print('No more frequent sets. Refer to earlier support candidates for the final frequent sets')
        break
    