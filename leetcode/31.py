#!/usr/bin/env python
"""
31. Next Permutation

Implement next permutation, which rearranges numbers into
the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it
as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column
and its corresponding outputs are in the right-hand column.
    1,2,3 -> 1,3,2
    3,2,1 -> 1,2,3
    1,1,5 -> 1,5,1
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        largest = float('-inf')
        for index in range(len(nums)-1, -1, -1):
            if nums[index] < largest:
                for j in range(len(nums)-1, index, -1):
                    if nums[index] < nums[j]:
                        self.swap(nums, index, j)
                        break
                i = index+1
                j = len(nums)-1
                while i < j:
                    self.swap(nums, i, j)
                    i += 1
                    j -= 1
                break
            largest = max(largest, nums[index])
        else:
            i = 0
            j = len(nums)-1
            while i < j:
                self.swap(nums, i, j)
                i += 1
                j -= 1

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_nextPermutation(self):
        nums = [1,2,3]
        expected = [1,3,2]
        self.s.nextPermutation(nums)        
        for index, elem in enumerate(nums):
            self.assertEqual(elem, expected[index])

    def test_nextPermutation2(self):
        nums = [3,2,1]
        expected = [1,2,3]
        self.s.nextPermutation(nums)
        for index, elem in enumerate(nums):
            self.assertEqual(elem, expected[index])

    def test_nextPermutation3(self):
        nums = [1,1,5]
        expected = [1,5,1]
        self.s.nextPermutation(nums)
        for index, elem in enumerate(nums):
            self.assertEqual(elem, expected[index])

    def test_nextPermutation4(self):
        nums = [1,3,4,2]
        expected = [1,4,2,3]
        self.s.nextPermutation(nums)
        # print nums, expected
        for index, elem in enumerate(nums):
            self.assertEqual(elem, expected[index])