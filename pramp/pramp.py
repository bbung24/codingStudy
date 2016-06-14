#!/usr/bin/env python

'''
This file is for pramp interview prep sessions.
'''
import unittest
#------------------------------------------------------------------------------
def eq_index_value(arr):
    """
    Given an array of sorted distinct integers named arr, write a function that
    returns an index i in arr for which arr[i] = i or -1 if no such index exists.

    Implement the most efficient solution possible, prove the correctness of 
    your solution and analyze its runtime complexity (in terms of n - the length of arr).

    Examples:

    Given arr = [-8,0,2,5] the function returns 2, since arr[2] = 2
    Given arr = [-1,0,3,6] the function returns -1, since no index in arr satisfies arr[i] = i
    """
    if len(arr) == 0:
        return -1
    return eq_index_value_helper(arr, 0, len(arr)-1)

def eq_index_value_helper(arr, low, high):
    if low > high:
        return -1
    mid = (low + high) / 2
    if mid == arr[mid]:
        return mid
    elif mid > arr[mid]:
        return eq_index_value_helper(arr, mid+1, high)
    else:
        return eq_index_value_helper(arr, low, mid-1)

#------------------------------------------------------------------------------
class Test(unittest.TestCase):
    def test_eq_index_value1(self):
        arr = [-8, 0, 2, 5]
        actual = eq_index_value(arr)
        self.assertEqual(2, actual)

    def test_eq_index_value2(self):
        arr = [-1, 0, 3, 6]
        actual = eq_index_value(arr)
        self.assertEqual(-1, actual)

    def test_eq_index_value3(self):
        arr = [-8, 0, 3, 5, 8]
        actual = eq_index_value(arr)
        self.assertEqual(-1, actual)

    def test_eq_index_value4(self):
        arr = [-8, 1, 3, 5, 8]
        actual = eq_index_value(arr)
        self.assertEqual(1, actual)

if __name__ == "__main__":
    unittest.main()