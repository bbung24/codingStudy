#!/usr/bin/env python
"""
135. Candy

There are N children standing in a line. Each child is assigned a rating value.

You are given candies to these children subjected to the following 
requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?
"""
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1 for a in ratings]
        candy = 1
        for index in range(1, len(ratings)):
            if ratings[index-1] < ratings[index]:
                candy += 1
                candies[index] = candy
            else:
                candy = 1
        for index in range(len(ratings)-2, -1, -1):
            if ratings[index+1] < ratings[index]:
                candy += 1
                candies[index] = max(candies[index], candy)
            else:
                candy = 1
        return sum(candies)

import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_candy(self):
        ratings = [2,4,2,6,1,7,8,9,2,1]
        expected = 19
        actual = self.s.candy(ratings)
        self.assertEqual(actual, expected)
