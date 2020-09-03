'''
Given a list of words, produce an algorithm that will return a list of all anagrams for a specific word

@Author: Tu Duong
@Date: 09/01/2020
'''

class AnagramsFinder:

    def __init__(self, word_list):

        self.lookup_dict = dict()

        for word in word_list:

            # word's signature is the letters of the word rearranged into alphabetical order
            # all anagrams of a given word will have the same signature
            word_signature = self._alphabetize(word)
            
            if word_signature in self.lookup_dict:
                self.lookup_dict[word_signature].append(word)
            else:
                self.lookup_dict[word_signature] = [word]

    def _alphabetize(self, word):
        char_list = list(word)
        char_list.sort() # sort all the letters by alphabetical order
        return ''.join(char_list)

    def find(self, given_word):

        if given_word is None:
            return None

        word_signature = self._alphabetize(given_word)
        return self.lookup_dict.get(word_signature, None)



import unittest

class TestAnagramsFinder(unittest.TestCase):

    def test_one_anagram(self):
        anagrams_finder = AnagramsFinder(['race', 'aaa', 'bbb'])
        given_word      = 'care'
        anagrams        = anagrams_finder.find(given_word)

        self.assertEqual(anagrams, ['race'])

    def test_multiple_anagram(self):
        anagrams_finder = AnagramsFinder(['race', 'aaa', 'bbb', 'cear', 'apple', 'care'])
        given_word      = 'care'
        anagrams        = anagrams_finder.find(given_word)

        self.assertEqual(anagrams, ['race', 'cear', 'care'])

    def test_zero_anagram(self):
        anagrams_finder = AnagramsFinder(['aaa', 'bbb', 'apple'])
        given_word      = 'care'
        anagrams        = anagrams_finder.find(given_word)

        self.assertEqual(anagrams, None)
    
    def test_empty_list(self): 
        anagrams_finder = AnagramsFinder([])
        given_word      = 'care'
        anagrams        = anagrams_finder.find(given_word)

        self.assertEqual(anagrams, None)
    
    def test_none_given_word(self): 
        anagrams_finder = AnagramsFinder(['aaa', 'bbb', 'apple'])
        given_word      = None
        anagrams        = anagrams_finder.find(given_word)

        self.assertEqual(anagrams, None)

    def test_empty_given_word(self): 
        anagrams_finder = AnagramsFinder(['aaa', 'bbb', 'apple'])
        given_word      = ''
        anagrams        = anagrams_finder.find(given_word)

        self.assertEqual(anagrams, None)

    def test_word_list_contains_empty_element(self): 
        anagrams_finder = AnagramsFinder(['aaa', '', 'bbb'])
        given_word      = ''
        anagrams        = anagrams_finder.find(given_word)

        self.assertEqual(anagrams, [''])
    

if __name__ == '__main__':
    unittest.main()