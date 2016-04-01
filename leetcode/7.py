"""
7. Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321 

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