#!/usr/bin/env python
"""
279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (
for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
return 2 because 13 = 4 + 9.
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        current = set([n])
        pss = self.getPerfectSquares(n)
        length = 0
        while True:
            next = set([])
            for c in current:
                for num in pss:
                    if num > c:
                        break
                    elif num < c:
                        next.add(c - num)
                    elif num == c:
                        return length + 1
            current = next
            length += 1

    def getPerfectSquares(self, n):
        nums = []
        i = 1
        while i * i <= n:
            nums.append(i*i)
            i += 1
        return nums
        
import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # def test_numSquares(self):
    #     n = 12
    #     expected = 3
    #     actual = self.s.numSquares(n)
    #     self.assertEqual(actual, expected)

    # def test_numSquares2(self):
    #     n = 150
    #     expected = 3
    #     actual = self.s.numSquares(n)
    #     self.assertEqual(actual, expected)

    # def test_numSquares3(self):
    #     n = 43
    #     expected = 3
    #     actual = self.s.numSquares(n)
    #     self.assertEqual(actual, expected)

    def test_numSquares4(self):
        n = 7168
        expected = 4
        actual = self.s.numSquares(n)
        self.assertEqual(actual, expected)
