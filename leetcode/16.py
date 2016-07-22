#!/usr/env/bin python
"""
16. 3Sum Closest

Given an array S of n integers, find three integers in S such
that the sum is closest to a given number, target. Return the
sum of the three integers. You may assume that each input would
have exactly one solution.
    For example, given array S = [-1,2,1,-4], and target = 1.
    The sum that is closest to the target is 2. (-1+2+1 = 2).
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = float('inf')
        closest = 0
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = len(nums) - 1
            need = target - nums[i]
            while start < end:
                s = nums[start] + nums[end]
                if s == need:
                    return target
                else:
                    tmp_target = s + nums[i]
                    tmp_diff = abs(target - tmp_target)
                    if tmp_diff < diff:
                        diff = tmp_diff
                        closest = tmp_target
                    if s < need:
                        start += 1
                    else:
                        end -= 1
        return closest
    
import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_threeSumClosest(self):
        nums = [-1,2,1,-4]
        target = 1
        expected = 2
        actual = self.s.threeSumClosest(nums, target)
        self.assertEqual(actual, expected)