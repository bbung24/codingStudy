#!/usr/bin/env python
"""
263. Ugly Number

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime
factor 7.

Note that 1 is typically treated as an ugly number.

"""
def isUgly(num):
    """
    :type num: int
    :rtype: bool
    """
    if num == 0:
        return False
    for n in (2,3,5):
        while num % n == 0:
            num /= n
    if num == 1:
        return True
    else:
        return False

import unittest
class TestClass(unittest.TestCase):
    def test_isUgly(self):
        sinput = [6,8,14]
        soutput = [True, True, False]
        for i, num in enumerate(sinput):
            actual = isUgly(num)
            self.assertEqual(soutput[i], actual)