#!/usr/bin/env python
"""
Project Euler #1 : Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these
multiples is 23. 

Find the sum of all the multiples of 3 or 5 below N.
"""
def find_sum(N):
    N -= 1
    total = 0
    remainder = N % 3
    last = (N - remainder) / 3
    total += (last*(last+1)/2)*3
    remainder = N % 5
    last = (N - remainder) / 5
    total += (last*(last+1)/2)*5
    remainder = N % 15
    last = (N - remainder) / 15
    total -= (last*(last+1)/2)*15
    return total

import unittest
class TestClass(unittest.TestCase):
    def test_find_sum(self):
        N = 10
        expected = 23
        actual = find_sum(N)
        self.assertEqual(expected, actual)

    def test_find_sum2(self):
        N = 100
        expected = 2318
        actual = find_sum(N)
        self.assertEqual(expected, actual)

    def test_find_sum3(self):
        N = 1000000000
        expected = 0
        actual = find_sum(N)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()