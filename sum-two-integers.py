'''
Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. 
Return true if the sum exists and return false if it does not.
Array = 5 7 1 2 8 4 3
Value = 10
True (7+3=10 or 2+8=10)
'''
def find_sum_of_two(int_array, value):

    # Set (implemented using Hash Table) is significantly faster when it comes to 
    # determining if an object is present in the set (as in x in s)
    # but is slower than list when it comes to iterating over its contents
    visited_set = set()
    
    for i in int_array:
        diff = value - i
        if diff in visited_set: # this is fast using Set
            return True

        visited_set.add(i)

    return False;


'''
find_sum_of_two([2, 1, 8, 4, 7, 3],3)
True
True
Succeeded

find_sum_of_two([2, 1, 8, 4, 7, 3],7)
True
True
Succeeded

find_sum_of_two([2, 1, 8, 4, 7, 3],20)
False
False
Succeeded

find_sum_of_two([5, 7, 1, 2, 8, 4, 3],1)
False
False
Succeeded

find_sum_of_two([5, 7, 1, 2, 8, 4, 3],2)
False
False
Succeeded

find_sum_of_two([5, 7, 1, 2, 8, 4, 3],7)
True
True
Succeeded
'''
