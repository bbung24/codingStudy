"""
9. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

SPOILER:

Some hints:

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev = self.reverse(x)
        if x - rev == 0:
            return True
        else:
            return False

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
    result = test.isPalindrome(-2147447412)
    print result