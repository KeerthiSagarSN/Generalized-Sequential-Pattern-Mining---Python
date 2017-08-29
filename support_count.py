# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 17:02:10 2017

@author: Keerthi
"""

def support_count_gen(cand_seq,database_seq,min_support,window_size,max_gap,min_gap,item_database_cust,item_database_time,k): 
    from numpy import size
    min_support_count_flag = []
    if k == 0:
        
        #support_cand_count = 1 # Counter for the number of candidate sequence available in the database sequence
        support_cand = []
        for i in xrange(0,len(cand_seq[k]),1): # Counter starts from 1 since the data has been given from 1. Pythonic way to start from 0 !!
            min_support_count = 0 # Minimum support for each candidate sequence is counted
            for j in xrange(1,len(database_seq),1): # Counter starts from 1 same reason as above
                
                
                if min_support_count >= min_support:
                    support_cand.append(cand_seq[k][i])
                    
                    break
                else:
                    for l in xrange(len(database_seq[j])):
                        
                        if cand_seq[k][i] in database_seq[j][l]:
                            min_support_count += 1 # Minimum support counter increased when the sequence is available in the database seq
                            break
                                        #if sub_support_count == size(cand_seq[k][i][jj]):
        return support_cand # Get the supporting frequent candidates                    
    else:
        print('nothing')
        
        support_cand = []
        for i in xrange(0,len(cand_seq[k]),1): # Counter starts from 1 since the data has been given from 1. Pythonic way to start from 0 !!
            min_support_count = 0 # Minimum support for each candidate sequence is counted
            for j in xrange(1,len(database_seq),1): # Counter starts from 1 same reason as above
                if iselement_there(item_database_cust,cand_seq[k][i],j-1): # Check if all elements of the candidate sequence exist for the candidate
                    if min_support_count >= min_support:
                        support_cand.append(cand_seq[k][i])
                            
                        break
                    else:
                         
                        min_support_count_flag = main_routine(item_database_time,cand_seq[k][i],window_size,max_gap,min_gap,j-1)
                        #print('min_support_count_flag',min_support_count_flag)
                        if min_support_count_flag:
                            min_support_count+= 1
                        
                        
                                
                                

        return support_cand                    
                        
        
    
# N -queens problem algorithm    
    
def main_routine(item_database_time,cand_seq,window_size,max_gap,min_gap,cust): # Sub-routine to calculate the minimum count based on timing constraints
    
    
     
    
    #sub_counter = len(cand_seq)

    # Maximum time in the candidate sequence list
    #print('cand_seq',cand_seq)
    tim_max = 0 
    for k in xrange(len(cand_seq)):
        from numpy import shape
        from copy import copy
        #print('cand_seq[k]',cand_seq[k])
        
        
        flat_list = cand_seq[k]
        print('cand_seq is',cand_seq)
        print('Flat_list',flat_list)
        for p in xrange(len(flat_list)):
            dum = []
            sss = shape(item_database_time[flat_list[p]][cust])
            sss = int(sss[0])
            dum = item_database_time[flat_list[p]][cust]
            for i in xrange(sss):
                dd = int(dum[i])    
                if dd > tim_max:
                    tim_max = dd                

        
        
    #tim_max = 90
    #print('I have crossed ')
    #print('Current Tim ', tim)
    
    # Adjacency matrix- For neighbor coonections
    adj_mat = {}
    adj_mat = [0] # Root node added to the adjoint matrix
    
    # Time constraint check
    def is_timeok(cand_seq,tim2,N):
        from numpy import shape
        
        #global tim
        tim = tim2
        size_ele = len(cand_seq[N])
        
        #print('Size of element is', size_ele)
        
        if size_ele == 1:
            for n in xrange(len(item_database_time[cand_seq[N][0]][int(cust)])):
                if N==0:
                    #print('tim+min_gap is', tim+min_gap)
                    #print('item_database_time[cand_seq[N][0]][int(cust)][n] is',item_database_time[cand_seq[N][0]][int(cust)][n])
                    if tim+min_gap <= item_database_time[cand_seq[N][0]][int(cust)][n]:
                        tim = copy(item_database_time[cand_seq[N][0]][cust][n])
                        '''
                        print('N is', N)
                        print('Candidate sequence is', cand_seq[N][0])
                        print('111 Time is ',tim)
                        pause(10)
                        '''
                        return True,tim
                    
                else:
                    #print('I have arrived here')
                    #print('tim+min_gap is', tim+min_gap)
                    #print('item_database_time[cand_seq[N][0]][int(cust)][n] is',item_database_time[cand_seq[N][0]][int(cust)][n])
                    if tim+min_gap <= item_database_time[cand_seq[N][0]][int(cust)][n] and tim+max_gap >= item_database_time[cand_seq[N][0]][cust][n]:
                        tim = copy(item_database_time[cand_seq[N][0]][cust][n])
                        '''
                        print('N is', N)
                        print('Candidate sequence is', cand_seq[N][0])
                        print('222 Time is ',tim)
                        print('I am returning value True 11')
                        pause(10)
                        '''
                        return True,tim
        if size_ele > 1:
            #print('cand_seq[N]', cand_seq[N])
            counter = len(cand_seq[N])
            
            k = 0
            
            while counter != 0 and k < (len(cand_seq[N])) :
                sub_cnt_shape = shape(item_database_time[cand_seq[N][k]][cust])
                sub_cnt = int(sub_cnt_shape[0])
                
                n = 0
                #print('Time abv loop is ',tim)
                while sub_cnt != 0:
                    #print('k is', k)
                    #print('n is', n)
                    if k ==0:
                        if N==0:
                            if tim+min_gap <= item_database_time[cand_seq[N][k]][cust][n]:
                                tim = copy(item_database_time[cand_seq[N][0]][cust][n])
                                '''
                                print('N is', N)
                                print('Candidate sequence is', cand_seq[N][k])
                                print('000 Time is ',tim)
                                print('Counter is', counter)
                                print('Sub-counter is ',sub_cnt)
                                pause(10)
                                '''
                                counter = counter - 1
                                sub_cnt = 0
                                n = n+1
                                
                                
                                
                                #print('Counter is', counter)
                            else:
                                
                                sub_cnt = sub_cnt - 1
                                n = n+1
                        else:
                            if tim+min_gap <= item_database_time[cand_seq[N][k]][cust][n] and tim+max_gap >= item_database_time[cand_seq[N][k]][cust][n]:
                                tim = copy(item_database_time[cand_seq[N][0]][cust][n])
                                '''
                                print('N is', N)
                                print('Candidate sequence is', cand_seq[N][k])
                                print('000kkk Time is ',tim)
                                print('Counter is', counter)
                                print('Sub-counter is ',sub_cnt)
                                pause(10)
                                '''
                                counter = counter - 1
                                sub_cnt = 0
                                n = n+1
                                
                                
                                
                                #print('Counter is', counter)
                            else:
                                #end_flag = end_flag - 1
                                sub_cnt = sub_cnt - 1
                                n = n+1
                            
                    if k> 0:
                        if tim+window_size >= item_database_time[cand_seq[N][k]][cust][n] and tim-window_size <= item_database_time[cand_seq[N][k]][cust][n]: 
                            #print('aaasssbb')
                            tim = copy(item_database_time[cand_seq[N][k]][cust][n])
                            counter = counter - 1
                            sub_cnt = 0
                            
                            
                            '''
                            print('N is', N)
                            print('Candidate sequence is', cand_seq[N][k])
                            print('kkk Time is ',tim)
                            print('Counter is', counter)
                            pause(10)
                            '''
                            n = n+1
                        else:
                            
                            
                            sub_cnt = sub_cnt - 1
                            n = n+1
                    
                    
                k += 1          
            
            if counter == 0:
                #print('I am returning value true')
                return True,tim
                    
        return False,tim
    
    
        
    # Find if the array is a list/flat 1D
    # Recursive function
    def sub_routine_recursive(cand_seq,adj_mat,tim1,N):
        # For the length of candidate sequence
        
        #global sub_contour
        #global tim
        #global sub_counter
        #print('sub-Counter bvb is', sub_counter)
        #print('N is', N)
        
        if N >= len(cand_seq):
            #print('I am true finally N is', N)
            return True
            
        # Terminating failure instances
        if tim1 >= tim_max:
            #print('Failure')
            
            return False
        
        else:
            is_timeok_result = is_timeok(cand_seq,tim1,N)
            #print (is_timeok_result)
            #print('I am blabla bla')
            #print('Value of N in sub_routing',N)
            if is_timeok_result[0]:
                # Add ajacent vertex/edge to the current node
                if N+1 not in adj_mat:
                    adj_mat = adj_mat + [N+1] 
                tim1 = is_timeok_result[1]
                #print('tim1 now is ', tim1)
                
                return sub_routine_recursive(cand_seq,adj_mat,tim1,N+1)
                
            else:
                for k in xrange(len(adj_mat)):
                    if adj_mat[k] != N: 
                        tim3 = is_timeok_result[1] + min_gap
                        #print('Value of N in sub_routing',N)
                        #print ('i am here in tim3, time is', tim3)
                        return sub_routine_recursive(cand_seq,adj_mat,tim3,adj_mat[k])
        
                
        return False        
        
        
                
                #return True
            
            
        #return False 
            
    # Calling the main function sub_routine_recursive    
    result_main_routine = sub_routine_recursive(cand_seq,adj_mat,-1000,0)            
    #print (result_main_routine)
    return result_main_routine
    
    
            
#    return support_cand # Return all the candidate sequences that weere supportted.            

# Check if first element of candidate sequence not available in the datasequence        
def iselement_there(item_database_cust,cand_seq,cust):
    from numpy import shape
    shape_list = shape(cand_seq) # To find if the list is 1d or multi-dimentionsal
    #print('shape list',shape_list)
    #print('cand_seq',cand_seq)
    if len(shape_list) == 2: # The list is multi-dimensional
    
        flat_list = [item for sublist in cand_seq for item in sublist] # Flatten a multi-dimensinal lisst to a 1d list
        #print('flat_list',flat_list)
    else:
        flat_list = cand_seq
        #print('flat_list',flat_list)
    counter = 0
    for j in xrange(len(flat_list)):
        if item_database_cust[flat_list[j]][cust]:
            counter += 1
    
    return counter == len(flat_list)
        
        
                