'''
Given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. 
Find x. The input array is not sorted.

@Author: Tu Duong
@Date: 09/02/2020
'''

def find_missing(input):

    n             = len(input) + 1  # input is missing 1 element. (+1) to include the missing element
    full_list     = range(1, n+1)   # range(n) is of exclusive nature, (n+1) to include the last element n
    full_list_sum = 0
    
    full_list_sum  = sum(full_list)
    input_sum      = sum(input)
    
    return (full_list_sum - input_sum)


import unittest

class TestFindMissing(unittest.TestCase):

    def test_find_missing_number(self):
        missed_num = find_missing([4, 5, 7, 2, 3, 1])
        self.assertEqual(missed_num, 6)


if __name__ == '__main__':
    unittest.main()