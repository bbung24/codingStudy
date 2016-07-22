#!/usr/bin/env python
"""
15. 3Sum

Given an array S of n integers, are there elements a,b,c in S
such that a+b+c = 0? Find all unique triplets in the array
which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1,0,1,2,-1,-4]
A solution set is:
[[-1,0,1],[-1,-1,2]]
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = len(nums) - 1
            need = nums[i] * -1
            while start < end:
                s = nums[start] + nums[end]
                if s == need:
                    result.append([nums[i], nums[start], nums[end]])
                    next = start
                    while next < len(nums) and nums[next] == nums[start]:
                        next += 1
                    start = next
                elif s < need:
                    start += 1
                else:
                    end -= 1
        return result

import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_threeSum(self):
        nums = [-1,0,1,2,-1,-4]
        expected = [[-1,0,1],[-1,-1,2]]
        actual = self.s.threeSum(nums)
        self.assertEqual(actual, expected)