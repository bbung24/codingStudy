#!/usr/bin/env python

'''
This file is for cracking the coding interview Chapter 17 : Hard
'''
import unittest
#------------------------------------------------------------------------------
def add_without_plus(a, b):
    '''
    17.1 Add Without Plus
    Write a function that adds two numbers. You should not use + or any arithmetic 
    operators.
    '''
    big = max(a,b)
    small = min(a,b)
    big_bin = bin(big)
    small_bin = bin(small)
    big_index = len(big_bin) - 1
    small_index = len(small_bin) - 1
    result = []
    flag = False
    while small_index >= 0:
        if small_bin[small_index] == 'b':
            break
        num, flag = add_helper(big_bin[big_index], small_bin[small_index], flag)
        result.insert(0, num)
        big_index -= 1
        small_index -= 1
    while big_bin[big_index] != 'b':
        num, flag = add_helper(big_bin[big_index], 0, flag)
        result.insert(0, num)
        big_index -= 1
    if flag:
        result.insert(0, '1')
    final_bin = ''.join(result)
    return int(final_bin, 2)

def add_helper(a, b, flag):
    if a == '1' and b =='1':
        if flag:
            return '1', True
        else:
            return '0', True
    elif a == '1' or b =='1':
        if flag:
            return '0', True
        else:
            return '1', False
    else:
        if flag:
            return '1', False
        else:
            return '0', False

def add_without_plus_sol(a, b):
    if b == 0:
        return a
    s = a ^ b
    c = (a & b) << 1
    return add_without_plus_sol(s, c)

#------------------------------------------------------------------------------
"""
17.2 Shuffle
Write a method to shuffle a deck of cards. It must be a perfect shuffle - in
other words, each of the 52! permutations of the deck has to be equally likely.
Assume that you are given a random number generator which is perfect.
"""

#------------------------------------------------------------------------------
class TestClass(unittest.TestCase):
    def test_add_without_sum(self):
        actual = add_without_plus(6, 4)
        self.assertEqual(10, actual)
        actual = add_without_plus(10, 12)
        self.assertEqual(22, actual)

    def test_add_without_sum_sol(self):
        actual = add_without_plus_sol(6, 4)
        self.assertEqual(10, actual)
        actual = add_without_plus_sol(10, 12)
        self.assertEqual(22, actual)

if __name__ == '__main__':
    unittest.main()