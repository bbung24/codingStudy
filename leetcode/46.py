#!/usr/bin/env python
"""
46. Permutations

Given a collection of distinct numbers, return all possible permutations

For example,
[1,2,3] have the following permutations:
[
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import math
        result = [nums]
        next = nums
        for a in xrange(math.factorial(len(nums))-1):
            next = self.nextPermutation(next)
            result.append(next)
        return result

    def nextPermutation(self, nums):
        """
        from leetcode problem 31.
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        new = [x for x in nums]
        i = len(new)-1
        for index in range(len(new)-2, -1, -1):
            if new[index] < new[index+1]:
                i = index
                break
        else:
            i = 0
        j = len(new) -1
        for index in range(len(new)-1, i, -1):
            if new[index] > new[i]:
                j = index
                break
        new[i], new[j] = new[j], new[i]
        i += 1
        j = len(new) -1
        while i < j:
            new[i], new[j] = new[j], new[i]
            i += 1
            j -= 1
        return new
        
import unittest
class TestClass(unittest.TestCase):
    """docstring for TestClass"""
    def setUp(self):
        self.s = Solution()

    def test_permute(self):
        nums = [1,2,3]
        expected = [
            [1,2,3],
            [1,3,2],
            [2,1,3],
            [2,3,1],
            [3,1,2],
            [3,2,1]
        ]
        actual = self.s.permute(nums)
        self.assertEqual(actual, expected)