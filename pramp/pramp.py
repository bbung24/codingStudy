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
def sentence_reverse(arr):
    """
    Sentence Reverse

    You are given an array of characters arr, which consists of sequences of 
    characters (words) separated by space characters. How can you most efficiently 
    reverse the order of words in the sentence? Explain and code your solution and 
    analyze the runtime and space complexity.

    For example:
    [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

    would turn into:
    [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'e', 'r', 'f', 'e', 'c', 't' ]
    """
    result = []
    words = []
    index = len(arr)-1
    word_index = 0
    word_length = 0
    while index >= 0:
        char = arr[index]
        result.append(char)
        if char == ' ' and word_length > 0:
            words.append((word_index, word_length))
            word_index += word_length + 1
            word_length = 0
        else:
            word_length += 1
        index -= 1
    if word_length > 0:
        words.append((word_index, word_length))
    for index, length in words:
        mirror_word(result, index, length)
    return result

def mirror_word(arr, index, length):
    for x in range(length/2):
        swap(arr, index+x, index+(length-1)-x)

def swap(arr, index1, index2):
    temp = arr[index2]
    arr[index2] = arr[index1]
    arr[index1] = temp

#------------------------------------------------------------------------------
def find_sum(arr, limit):
    """
    Given a package with a weight limit and an array arr of item weights, 
    how can you most efficiently find two items with sum of weights that equals 
    the weight limit?

    Your function should return 2 such indices of item weights or -1 
    if such pair doesn't exist.
    What is the runtime and space complexity of your solution?
    """
    flag = {}
    for index, number in enumerate(arr):
        pair = limit - number
        if pair in flag:
            return [flag[pair], index]
        else:
            flag[number] = index
    return -1

#------------------------------------------------------------------------------
def shifted_array_search(arr, num):
    """
    Shifted Array Search

    1. Find a given number num in a sorted array arr: --> Do Binary Search
    arr = [2, 4, 5, 9, 12, 17] 

    2. If the sorted array arr is shifted left by an unknown offset and 
    you don't have a pre-shifted copy of it, how would you modify your method 
    to find a number in the shifted array?
    shiftArr = [9, 12, 17, 2, 4, 5]

    Explain and code an efficient solution and analyze its runtime complexity
    if num doesn't exist in the array, return -1
    """
    begin = 0
    end = len(arr)-1
    while begin <= end:
        mid = (begin + end) / 2
        if arr[mid] == num:
            return mid
        elif arr[end] == num:
            return end
        elif arr[begin] == num:
            return begin
        if num > arr[mid]:
            # Case where number looking for is greater than mid
            if arr[end] > num: # if right end is greater than num, look right.
                begin = mid + 1
            elif arr[begin] > arr[mid]: # if there is shift in left side, look left.
                end = mid - 1
            else: # if there is shift in right side, still need to look right.
                begin = mid + 1
        elif num < arr[mid]: 
            # Case where number looking for is less than mid
            if arr[begin] < num: # if left begin is less than num look left.
                end = mid - 1
            elif arr[end] < arr[mid]: # if there is shift in right side, look right.
                begin = mid + 1
            else: # if there is shift in left side, still need to look left.
                end = mid - 1
    return -1

#------------------------------------------------------------------------------
class Test(unittest.TestCase):
    def test_shifted_array_search(self):
        shiftArr = [9, 12, 17, 2, 4, 5]
        num = 12
        actual = shifted_array_search(shiftArr, num)
        self.assertEqual(1, actual)
        num = 4
        actual = shifted_array_search(shiftArr, num)
        self.assertEqual(4, actual)
        num = 3
        actual = shifted_array_search(shiftArr, num)
        self.assertEqual(-1, actual)

    def test_find_sum(self):
        arr = [1, 2, 3, 4]
        limit = 6
        actual = find_sum(arr, limit)
        self.assertEqual([1,3], actual)

    def test_sent_rev1(self):
        arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
        expected = [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't' ]
        actual = sentence_reverse(arr)
        self.assertEqual(expected, actual)

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