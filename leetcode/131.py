#!/usr/bin/env python
"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a
palindrome.

Return all possible palindrome partitioning of s.

For example, given s = 'aab',
Return 
[['aa','b'], ['a','a','b']]
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.splitstring(s, [], result)
        return result
        
    def splitstring(self, s, path, result):
        if not s:
            result.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.splitstring(s[i:], path+[s[:i]], result)

    def isPalindrome(self, s):
        return s == s[::-1]

import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_partition(self):
        s = 'aab'
        print self.s.partition(s)