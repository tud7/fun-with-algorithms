'''
Implement an algorithm to determine if a string has all unique characters

@Author: Tu Duong
@Date: 09/22/2020
'''

MAX_UNIQUE_CHAR_NUMBER = 128

def is_unique(in_string):

    if len(in_string) > MAX_UNIQUE_CHAR_NUMBER:
        return False
    
    unique_chars = []

    for c in in_string:
        if c in unique_chars:
            return False
        else:
            unique_chars.append(c)

    return True


import unittest

class TestIsUnique(unittest.TestCase):

    def test_unique_string(self):
        self.assertEqual(is_unique('abcd'), True)
        self.assertEqual(is_unique('qwert123$%'), True)
        self.assertEqual(is_unique('qazwsxedcrfvtgbyhnujmik'), True)
    
    def test_non_unique_string(self):
        self.assertEqual(is_unique('abcad'), False)
        self.assertEqual(is_unique('uniqueu'), False)
        self.assertEqual(is_unique('qazwsxedcrfvtgbyhnujmiaq'), False)

    def test_empty_string(self):
        self.assertEqual(is_unique(''), True)


if __name__ == '__main__':
    unittest.main()