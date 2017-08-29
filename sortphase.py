# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 02:36:46 2017

@author: Keerthi
"""

import numpy as np


# Need to do  sorting later



from collections import defaultdict
db_ini = {}
db_ini = [[0,30,90],[0,20,30],[1,35,10,20],[1,15,30],[1,20,40,60,70],[2,25,30,50,70],[3,20,30],[3,25,40,70],[3,30,90],[4,12,90]]

# Sort the candidate list - Sort by time candidate
db = sorted(db_ini, key=lambda tup: tup[1])
# Sort the candiatate list - Sort by candidate list
db = sorted(db,key = lambda tup: tup[0])
# Sort 

# Customer sequence database

# Get the number of candidate list from the database list
cno = max(l[0] for l in db)

# Function to retrieve based list based on element value
# Iterate through the database to add the elements in the customer sequence database
def find_list(list_input, index,value):
    return [listdb for listdb in list_input if listdb[index] == value]


# Creating a sequence candidate item list
cseq = {}


for  i in xrange(cno+1):
    cseq[i] = [i]

for k in xrange(cno+1):
    # intermediate array
    # Declare interarray
    #cseq[k] = [k]
    inter_arr = {}
    inter_arr = find_list(db,0,k)
    
    for j in xrange(len(inter_arr)):
        # Get the size of the list of each candidate at a specific transaction - We can get the number of items from this
        new_arr = inter_arr[j]
        append_arr = new_arr[2:] # First element is candidate list, second element is transaction time, so from third element is the item list
        cseq[k] = cseq[k]+[append_arr]


    