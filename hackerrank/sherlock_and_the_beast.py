#!/usr/bin/env python
"""
Sherlock and The Beast

Sherlock Holmes suspects his archenemy, Professor Moriaty, is once again 
plotting something diabolical. Sherlock's companion, Dr. Watson, suggests
Moriaty may be responsible for MI6's recent issues with their supercomputer, 
The Beast. 

Shortly after resolving to investigate, Sherlock receives a note from Moriaty
boasting about infecting The Beast with a virus; however, he also gives him a
clue - a number, N. Sherlock determines the key to removing the virus is to find
the largest Decent Number having N digits.

A Decent Number has the following properties:
    1. Its digits can only be 3's and/or 5's
    2. The number of 3's it contains is divisible by 5.
    3. The number of 5's it contains is divisible by 3.
    4. If there are more than one such number, we pick the largest one.

Moriaty's virus shows a clock counting down th The Beast's destruction, and time is 
running out fast. Your task is to help Sherlock find the key before The Beast is destroyed!

Input format :
T , denoting the number of test cases
N, detailing the number of digits in the number.

Output format :
print the largest Decent Number having N digits; if no such number exists, tell Sherlock by 
printing -1.

"""
import unittest

def find_largest(N):
    fives = ['5' for a0 in xrange(N)]
    threes = []
    for a0 in xrange(N):
        if len(fives) % 3 == 0 and len(threes) % 5 == 0:
            if len(fives) == 0:
                return int(''.join(threes))
            elif len(threes) == 0:
                return int(''.join(fives))
            else:
                return int(''.join(fives+threes))
        else:
            fives.pop()
            threes.append('3')
    if len(threes) % 5 == 0:
        return int(''.join(threes))
    return -1


class TestClass(unittest.TestCase):
    def test_sample(self):
        t = 4
        sinput = [1,3,5,11]
        soutput = [-1,555,33333,55555533333]
        for i, n in enumerate(sinput):
            actual = find_largest(n)
            expected = soutput[i]
            self.assertEqual(expected, actual)
