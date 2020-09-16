'''
Given a dictionary of words and a large input string, find out whether the
input string can be completely segmented into the words of a given dictionary.
For example:
dictionary: {apple, apple, pear, pie}
string: applepie  --> True
string: applepeer --> False

@Author: Tu Duong
@Date: 09/16/2020
'''

def can_segment_string(string, dictionary):
  
    if string in dictionary:
        return True

    word1 = ''
    word2 = ''
    for i in range(0, len(string)): 
        word1 = string[:i]
        if word1 in dictionary:
            word2 = string[i:]
            if word2 in dictionary or can_segment_string(word2, dictionary):
                return True

    return False


import unittest

class TestStringSegmentation(unittest.TestCase):

    def test_true(self):

        result = can_segment_string('applepie', {'apple', 'peach', 'pear', 'pie'})
        self.assertEqual(result, True)

        result = can_segment_string('hellonow',{'on', 'hell', 'ow', 'hellothere'})
        self.assertEqual(result, True)

        result = can_segment_string('hellonow',{'hellonow', 'hell', 'ow', 'hellothere'})
        self.assertEqual(result, True)

    def test_false(self):

        result = can_segment_string('applepeer',{'apple', 'peach', 'pear', 'pie'})
        self.assertEqual(result, False)

    def test_empty_string(self):
      
        result = can_segment_string('',{'hellonow', 'hell', 'ow', 'hellothere'})
        self.assertEqual(result, False)

        result = can_segment_string('',{'hellonow', '', 'ow', 'hellothere'})
        self.assertEqual(result, True)

        result = can_segment_string('',{})
        self.assertEqual(result, False)


if __name__ == '__main__':

    unittest.main()
