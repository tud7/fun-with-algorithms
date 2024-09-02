"""
Leetcode #22: Generate Parentheses
@Author: Tu Duong
@Date: 09/02/2024
"""

#pylint: disable=missing-function-docstring,pointless-string-statement,line-too-long

import unittest

cache = {0:0, 1:1, 2:2}

def generate_parentheses(n: int) -> int:
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    Example 1:

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
    Example 2:

    Input: n = 1
    Output: ["()"]
    """

    """
    Notes:
                                            0,0, ""
                                             
                                            1,0, "("

                1,1, "()"                                           2,0, "(("

                2,1, "()("                       3,0, "((("                           2,1, "(()"

        2,2, “()()”     3,1, “()((”              3,1, “((()”                  3,1, “(()(”         2,2, “(())”

        3,1, “()()(”    3,2, “()(()”             3,2, “((())”                 3,2, “(()()”        3,2, “(())(”

        3,3, “()()()”   3,3, “()(())”            3,3, “((()))”                3,3, “(()())”       3,3, “(())()”

    """
    def rescursive_find(num_open, num_close, combination):

        if num_open == n and num_close == n:
            combinations.append(combination) # once found, append the combination to the result list
            return

        # Note: using 2 if statements instead of if else
        if num_open < n:
            rescursive_find(num_open+1, num_close, combination + "(")
        if num_close < num_open:
            rescursive_find(num_open, num_close+1, combination + ")")

    combinations = []
    rescursive_find(0, 0, "")

    return combinations


class MyTestCase(unittest.TestCase):
    """Test cases"""

    def test_climb_stairs(self):
        self.assertEqual(generate_parentheses(1), ["()"])
        self.assertEqual(generate_parentheses(3), ["((()))","(()())","(())()","()(())","()()()"])


if __name__ == '__main__':
    unittest.main()
