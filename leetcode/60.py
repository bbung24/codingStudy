#!/usr/bin/env python
"""
60. Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):
    1. "123"
    2. "132"
    3. "213"
    4. "231"
    5. "312"
    6. "321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        numbers = range(1,n+1)
        facto = math.factorial(n)
        result = []
        while len(numbers) > 0:
            facto /= len(numbers)
            index, mod = divmod(k, facto)
            if mod == 0:
                index -= 1
            k = mod
            result.append(str(numbers.pop(index)))
        return ''.join(result)



import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_getPermutation(self):
        n = 3
        k = 2
        expected = "132"
        actual = self.s.getPermutation(n,k)
        self.assertEqual(actual, expected)

    def test_getPermutation2(self):
        n = 3
        k = 3
        expected = "213"
        actual = self.s.getPermutation(n,k)
        self.assertEqual(actual, expected)