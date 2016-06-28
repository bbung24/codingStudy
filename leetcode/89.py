#!/usr/bin/env python
"""
89. Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the 
sequence of gray code. A gray code sequence must begin with 0.

For example, givne n = 2, return [0,1,3,2]. Its gray code sequence is:
00 - 0
01 - 1
11 - 3
10 - 2

Note:

For a given n, a gray code sequence is not uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
"""
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(n):
            result += [x + pow(2,i) for x in reversed(result)]
        return result
        
import unittest 
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_grayCode(self):
        expected = [0,1,3,2]
        actual = self.s.grayCode(2)
        self.assertEqual(actual, expected)
