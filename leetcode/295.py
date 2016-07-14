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
from heapq import heappush, heappop, heapify, heappushpop
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left = []
        self.right = []
        self.even_length = True

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.left) == 0 or num <= -1*self.left[0]:
            if len(self.left) > len(self.right):
                tmp_num = heappushpop(self.left, -1*num)
                heappush(self.right, -1*tmp_num)
            else:
                heappush(self.left, -1*num)
        elif len(self.right) == 0 or num >= self.right[0]:
            if len(self.right) > len(self.left):
                tmp_num = heappushpop(self.right, num)
                heappush(self.left, -1*tmp_num)
            else:
                heappush(self.right, num)
        else:
            if len(self.left) > len(self.right):
                tmp_num = heappushpop(self.left, -1*num)
                heappush(self.right, -1*tmp_num)
            else:
                heappush(self.left, -1*num)
        self.even_length = not self.even_length
        # print self.left, self.right, self.even_length

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.even_length:
            if len(self.right) == 0:
                median = -1*self.left[0]
            else:
                median = (-1*self.left[0] + self.right[0]) / 2.0
        else:
            if len(self.left) > len(self.right):
                median = -1*self.left[0]
            else:
                median = self.right[0]
        return round(median, 5)

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

    def test_median_finder3(self):
        self.s.addNum(12)
        expected = 12.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(10)
        expected = 11.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(13)
        expected = 12.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(11)
        expected = 11.50000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(5)
        expected = 11.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(15)
        expected = 11.50000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(1)
        expected = 11.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(11)
        expected = 11.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(6)
        expected = 11.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(17)
        expected = 11.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(14)
        expected = 11.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(8)
        expected = 11.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(17)
        expected = 11.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(6)
        expected = 11.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(4)
        expected = 11.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(16)
        expected = 11.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(8)
        expected = 11.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(10)
        expected = 10.50000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(2)
        expected = 10.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(12)
        expected = 10.50000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        self.s.addNum(0)
        expected = 10.00000
        actual = self.s.findMedian()
        self.assertEqual(actual, expected)
        
# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()