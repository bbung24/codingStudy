#!/usr/bin/env python
"""
216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only
numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
"""
from itertools import combinations
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        for i in combinations(range(1,10), k):
            if sum(i) == n:
                result.append(list(i))
        return result


import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_combinationSum3(self):
        k = 3
        n = 7
        expected = [[1,2,4]]
        actual = self.s.combinationSum3(k, n)
        self.assertEqual(actual, expected)

    def test_combinationSum3_2(self):
        k = 3
        n = 9
        expected = [[1,2,6],[1,3,5],[2,3,4]]
        actual = self.s.combinationSum3(k, n)
        self.assertEqual(actual, expected)