#!/usr/bin/env python
"""
Objective 
Today, we're building on our knowledge of Arrays by adding another dimension. 
Check out the Tutorial tab for learning materials and an instructional video!

Context 
Given a  2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in 
this pattern in A's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in A, and an hourglass sum is the sum of an 
hourglass' values.

Task 
Calculate the hourglass sum for every hourglass in A, then print the maximum 
hourglass sum.

Input Format

There are 6 lines of input, where each line contains 6 space-separated 
integers describing 2D Array A; every value in A will be in the inclusive 
range of -9 to 9.

Output Format

Print the largest (maximum) hourglass sum found in A.
"""

#!/bin/python

import sys

def hourglass_sum(arr, row, col):
    """
    find sum of hourglass given start index
    """
    s = 0 #sum
    for i in range(3):
        s += arr[row][col+i]
    s += arr[row+1][col+1]
    for i in range(3):
        s += arr[row+2][col+i]
    return s

def find_maximum_hourglass_sum(arr):
    """
    find maximum sum of hourglass given array
    """
    rows = len(arr)
    cols = len(arr[0])
    maximum = -9 * 7
    for row in range(rows-2):
        for col in range(cols-2):
            maximum = max(maximum, hourglass_sum(arr, row, col))
    return maximum

arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

print find_maximum_hourglass_sum(arr)
