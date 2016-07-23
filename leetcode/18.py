#!/usr/bin/env python
"""
18. 4Sum

Given an array S of n integers, are there elements a,b,c and d
in S such that a + b + c + d = target? Find all unique quadruplets
in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
    [-1, 0, 0, 1],
    [-2, -1, 1, 2],
    [-2, 0, 0, 2]
]
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = set([])
        two_sums = {}
        nums.sort()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                s = target - (nums[i] + nums[j])
                if not s in two_sums:
                    two_sums[s] = []
                two_sums[s].append([i,j])
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                s = nums[i] + nums[j]
                if s in two_sums:
                    for elem in two_sums[s]:
                        if not i in elem and not j in elem:
                            candidate = [nums[elem[0]], nums[elem[1]], nums[i], nums[j]]
                            candidate.sort()
                            result.add(tuple(candidate))
        return map(list, list(result))
        
import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_fourSum(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        expected = [[-1, 0, 0, 1],[-2, -1, 1, 2],[-2, 0, 0, 2]]
        actual = self.s.fourSum(nums, target)
        self.assertEqual(actual, expected)