#!/usr/bin/env python
"""
295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list 
is even, there is no middle value. So the median is the mean of the two middle
value.

Examples:

[2,3,4], the median is 3.
[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:
    void addNum(int num) - Add a integer number from the data stream to the 
        data structure.
    double findMedian() - Return the median of all elements so far.

"""
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        for index, elem in enumerate(self.nums):
            if elem >= num:
                self.nums.insert(index, num)
                return
        else:
            self.nums.append(num)


    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.nums) % 2 == 0:
            # length is even so we need to get mean of the two middle value.
            mid1 = (len(self.nums)-1) / 2
            mid2 = mid1+1
            median = (self.nums[mid1] + self.nums[mid2]) / 2.0
            return median
        else:
            mid = (len(self.nums)-1) / 2
            median = float(self.nums[mid])
            return median

import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = MedianFinder()

    def test_median_finder(self):
        self.s.addNum(1)
        self.s.addNum(2)
        expected = 1.5
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(3)
        expected = 2
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)

    def test_median_finder2(self):
        self.s.addNum(6)
        expected = 6.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(10)
        expected = 8.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(2)
        expected = 6.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(6)
        expected = 6.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(5)
        expected = 6.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(0)
        expected = 5.50000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(6)
        expected = 6.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(3)
        expected = 5.50000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(1)
        expected = 5.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(0)
        expected = 4.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(0)
        expected = 3.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()