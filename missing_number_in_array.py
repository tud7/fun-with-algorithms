'''
Given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. 
Find x. The input array is not sorted.
'''

def find_missing(input):

    n             = len(input) + 1  # input is missing 1 element. (+1) to include the missing element
    full_list     = range(1, n+1)   # range(n) is of exclusive nature, (n+1) to include the last element n
    full_list_sum = 0
    
    full_list_sum  = sum(full_list)
    input_sum      = sum(input)
    
    return (full_list_sum - input_sum)
