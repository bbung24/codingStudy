#!/usr/bin/env python
"""
80. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What is duplicates are allowed at most twice ?

For example,
Given sorted array nums = [1,1,1,2,2,3].

Your function should return lengh = 5, with the first five elements of nums 
being, 1,1,2,2 and 3. It doesn't matter what you leave beyond the new length.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        result = [nums[0]]
        current_num = nums[0]
        count = 1
        for index in range(1,len(nums)):
            if nums[index] != current_num:
                result.append(nums[index])
                current_num = nums[index]
                count = 1
            elif count < 2:
                result.append(nums[index])
                count += 1
        for index, elem in enumerate(result):
            nums[index] = elem
        return len(result)

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_removeDuplicates(self):
        nums = [1,1,1,2,2,3]
        expected = 5
        expected_array = [1,1,2,2,3]
        actual = self.s.removeDuplicates(nums)
        self.assertEqual(actual, expected)
        for i in range(len(expected_array)):
            self.assertEqual(nums[i], expected_array[i])
