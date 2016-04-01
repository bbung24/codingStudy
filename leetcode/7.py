"""
7. Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321 

SPOILER:

Have you thought about this?

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

-- For this problem, think of system as having 32-bit integer.
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # import sys
        max_int = (2 ** 31 -1)
        min_int = -max_int-1
        flag = self.isNeg(x)
        x = int(str(abs(x))[::-1])
        if flag:
            x *= -1
            if x < min_int:
                return 0
        if x > max_int:
            return 0
        return x

    def isNeg(self, x):
        return x < 0

if __name__ == "__main__":
    test = Solution()
    result = test.reverse(1000000003)
    print result, result == 0