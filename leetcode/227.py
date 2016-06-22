#!/usr/bin/env python
"""
227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces ' '.
The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2" = 5

Note: Do not use the eval built-in library function

"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        l = []
        elem = []
        for c in s:
            if c != ' ':
                if c == '+' or c == '-' or c =='*' or c =='/':
                    if len(elem) > 0:
                        l.append(''.join(elem))
                        elem = []
                    l.append(c)
                else:
                    elem.append(c)
        if len(elem) > 0:
            l.append(''.join(elem))
        if len(l) < 2:
            return int(l[0])
        index = 0
        tmp = []
        while index < len(l):
            if l[index] == '*':
                prev_num = int(l[index-1])
                next_num = int(l[index+1])
                result = prev_num * next_num
                l[index+1] = result
                tmp.pop()
                tmp.append(result)
                index += 1
            elif l[index] == '/':
                prev_num = int(l[index-1])
                next_num = int(l[index+1])
                result = prev_num / next_num
                l[index+1] = result
                tmp.pop()
                tmp.append(result)
                index += 1
            else:
                tmp.append(l[index])
            index += 1
        l = tmp
        index = 0
        while index < len(l):
            if l[index] == '+':
                prev_num = int(l[index-1])
                next_num = int(l[index+1])
                result = prev_num + next_num
                l[index+1] = result         
                index += 1  
            elif l[index] == '-':
                prev_num = int(l[index-1])
                next_num = int(l[index+1])
                result = prev_num - next_num
                l[index+1] = result
                index += 1
            index += 1
        return l[len(l)-1]

import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_calculate(self):
        test_input = "3+2*2"
        expected = 7
        actual = self.s.calculate(test_input)
        self.assertEqual(expected, actual)

    def test_calculate2(self):
        test_input = " 3/2 "
        expected = 1
        actual = self.s.calculate(test_input)
        self.assertEqual(expected, actual)

    def test_calculate3(self):
        test_input = " 3+5 / 2"
        expected = 5
        actual = self.s.calculate(test_input)
        self.assertEqual(expected, actual)  

    def test_calculate4(self):
        test_input = " 42"
        expected = 42
        actual = self.s.calculate(test_input)
        self.assertEqual(expected, actual)

    def test_calculate5(self):
        test_input = " 42 + 2"
        expected = 44
        actual = self.s.calculate(test_input)
        self.assertEqual(expected, actual)

    def test_calculate6(self):
        test_input = "1+1+1"
        expected = 3
        actual = self.s.calculate(test_input)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()