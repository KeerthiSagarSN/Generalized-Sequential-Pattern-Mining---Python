# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 01:05:59 2017

@author: Keerthi
"""

def database_seqfn(proc_db,cust_size):
    # Create an array
    database_set_time = {} # All times listed for every candidate
    database_seq = {} # All items listed for every candidate
    
    for k in xrange(0,cust_size):
        
        dum = []
        dum2 = []
        for i in xrange(len(proc_db)):
            if proc_db[i][1] == k:
                dum1 = proc_db[i][0]
                dum3 = proc_db[i][3:]
                dum .append(dum1)
                dum2.append(dum3)
        #database_set_time[k]  = dum
        database_seq[k] = dum2
    return database_seq
                    
    
        
def item_database(database_seq,singleton_arr):
    item_database_cust = {} # All items are enlisted with respect to time and 
    item_database_time = {}
    
    
    for j in xrange(len(singleton_arr)):
        
        dum2 = []
        item_flag_dum = []
        for cust in xrange(len(database_seq)):
            dum = []
            dum1 = []
            item_flag = False    
            for k in xrange(len(database_seq[cust])):
                if j in database_seq[cust][k]:
                    item_flag = True
                    dum  = k # Time column
                    dum1.append(dum)
                
            item_flag_dum.append(item_flag)   
            dum2.append(dum1) # Entire list of time in a dummy array
            
                
        item_database_time[j] = dum2
        
        item_database_cust[j] = item_flag_dum
    
    return item_database_cust,item_database_time
        
        
        
    