#!/usr/bin/env python
"""
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in 
the diagram below). 

The robot can only move either down or right at any point in time. The robot
is trying to reach the bottom-right corner of the grid (marked 'Finish' in the 
diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        num_paths = [[0 for j in range(n)] for i in range(m)]
        num_paths[0][0] = 1
        for i in range(m):
            for j in range(n):
                count = 0
                if i > 0:
                    count += num_paths[i-1][j]
                if j > 0:
                    count += num_paths[i][j-1]
                if count != 0:
                    num_paths[i][j] = count
        return num_paths[m-1][n-1]

import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_uniquePaths(self):
        expected = 1
        actual = self.s.uniquePaths(1,2)
        self.assertEqual(expected, actual)

    def test_uniquePaths2(self):
        expected = 28
        actual = self.s.uniquePaths(3,7)
        self.assertEqual(expected, actual)

    def test_uniquePaths3(self):
        expected = 193536720
        actual = self.s.uniquePaths(23,12)
        self.assertEqual(expected, actual)