#!/usr/bin/env python
"""
122. Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times). However, you may not engage in
multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy if next int is greater than current
        # sell if next int is less than current
        if len(prices) < 1:
            return 0
        profit = 0
        current_buy = 0
        bought = False
        for index in xrange(len(prices)-1):
            if not bought and prices[index] < prices[index+1]:
                current_buy = prices[index]
                bought = True
            elif bought and prices[index] > prices[index+1]:
                profit += prices[index] - current_buy
                bought = False
        else:
            if bought and prices[len(prices)-1] > current_buy:
                profit += prices[len(prices)-1] - current_buy
        return profit

import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution().maxProfit

    def test_maxProfit(self):
        sinput = []
        expected = 0
        actual = self.s(sinput)
        self.assertEqual(expected, actual)

    def test_maxProfit2(self):
        sinput = [1,5,6,7,1,2,6,8,8,3,324,523,5]
        expected = 533
        actual = self.s(sinput)
        self.assertEqual(expected, actual)