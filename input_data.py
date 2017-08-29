# -*- coding: utf-8 -*-
"""
Created on Mon Aug 07 18:40:17 2017

@author: Keerthi
"""

from copy import copy,deepcopy
def input_db(input_filename):
    input_db = []
    customer_size = 0
    with open(input_filename) as inputfile:
        for line in inputfile:
            input_db.append(line.strip().split())
            
    input_database = deepcopy(input_db)
    item_db = {} # Mapping string to integer
    item_db_reverse = {} # Reverse mapping integer to string
    int_count = 0
    for i in xrange(len(input_db)):
        dum = []
        dum = list(input_db[i])
        for k in xrange(3,len(dum),1):
            if dum[k] not in item_db:
                item_db[dum[k]] = int_count
                item_db_reverse[int_count] = dum[k]
                int_count+= 1
    
    
    # Numpy array for faster computation
    
    # Processed database
    proc_db = list(input_db)
    for j in xrange(len(input_db)):
        dum = list(input_db[j])
        proc_db[j][0] = int(dum[0])
        
        
        # Counting the number of customers
        if int(dum[1]) > customer_size: 
            customer_size = int(dum[1])
        for l in xrange(1,3,1):
            proc_db[j][l] = int(dum[l])
        # Sorting the itemsets inside each transactions. This would reduce later candidate generation combinations
        
        dumsort = []
        for kk in xrange(3,len(dum),1):
            dumsort.append(int(item_db[dum[kk]]))
            
        dumsort.sort()
        for p in xrange(3,len(dum),1):
            proc_db[j][p] = dumsort[p - 3]
    return proc_db,input_database,item_db_reverse,customer_size
    

    