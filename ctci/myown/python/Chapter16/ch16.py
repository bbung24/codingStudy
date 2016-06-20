#!/usr/bin/env python

'''
This file is for cracking the coding interview Chapter 16 : Moderate
'''

import unittest
#------------------------------------------------------------------------------
def num_swap(a, b):
    '''
    16.1 Number Swapper
    Write a function to swap a number in place (that is, without temporary variables).
    '''
    if a > b:
        a += b
        b = a - b
        a = a - b
    else:
        b += a
        a = b - a
        b = b - a
    return a, b

def num_swap_sol(a, b):
    """
    Solution from the book uses xor operator
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

#------------------------------------------------------------------------------
"""
16.2 Word Frequencies
Design a method to find the frequency of occurrences of any given word in 
a book. What if we were running this algorithm multiple times? 
"""
class Book(object):
    def __init__(self, context):
        if type(context) != list:
            raise Exception('Context needs to be given as list of strings.')
        self.freq = {}
        self.context = context
        self.calc_word_freq(context)

    def calc_word_freq(self, book):
        for word in book:
            word = word.lower()
            if word in self.freq:
                self.freq[word] += 1
            else:
                self.freq[word] = 1

    def word_freq(self, word):
        if word == None: return -1
        return self.freq.get(word.lower(), -1)

#------------------------------------------------------------------------------
def intersection(line1, line2):
    """
    16.3 Intersection
    Given two straight line segments (represented as a start point and an end point),
    compute the point of intersection, if any.
    """
    # If slope is same,
    #   if intercept is same, intersect
    #   if intercept is different, don't intersect
    if (line1.slope == line2.slope and
        line1.intercept != line2.intercept):
            raise Exception('No intersection')
    for x in range(line1.start.x, line1.end.x+1):
        y = line1.get_y(x)
        if line2.is_point(x, y):
            return (x, y)
    raise Exception('No intersection')

class Line(object):
    def __init__(self, start, end):
        delta_y = end.y - start.y
        delta_x = end.x - start.x
        self.slope = delta_y / delta_x
        self.intercept = end.y - self.slope * end.x
        self.start = start
        self.end = end

    def get_y(self, x):
        return self.slope * x + self.intercept

    def is_point(self, x, y):
        return y == self.get_y(x)

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

#------------------------------------------------------------------------------
class TestClass(unittest.TestCase):
    def test_intersect(self):
        s1 = Point(1,2)
        s2 = Point(4,8)
        s3 = Point(3,2)
        s4 = Point(1,6)
        l1 = Line(s1, s2)
        l2 = Line(s4, s3)
        actual = intersection(l1, l2)
        self.assertEqual((2,4), actual)

    def test_num_swap(self):
        actual = num_swap(6, 4)
        self.assertEqual((4, 6), actual)

    def test_num_swap_sol(self):
        actual = num_swap_sol(6, 4)
        self.assertEqual((4, 6), actual)

if __name__ == '__main__':
    unittest.main()