"""
8. String to Integer (atoi)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, 
please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). 
You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. 
If you still see your function signature accepts a const char * argument, 
please click the reload button to reset your code definition. 

SPOILER:

Requirements for atoi:

The function first discards as many whitespace characters as necessary 
until the first non-whitespace character is found. Then, starting from this character, 
takes an optional initial plus or minus sign followed by as many numerical digits as possible, 
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, 
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, 
or if no such sequence exists because either str is empty or it contains only whitespace characters, 
no conversion is performed.

If no valid conversion could be performed, a zero value is returned. 
If the correct value is out of the range of representable values, 
INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        # empty string
        if str == "":
            return 0
        str = str[::-1]
        integer = 0
        nth = 0
        for index, num in enumerate(str):
            digit = self.number(num)
            if digit != None:
                integer += digit * (10 ** nth)
                nth += 1
            elif index == (len(str)-1) and self.isSymbol(num):
                if num == '-':
                    integer *= -1
            else:
                integer = 0
                nth = 0
        # overflow int
        return self.checkOverFlow(integer)

    def checkOverFlow(self, num):
        max_int = (2 ** 31 -1)
        min_int = -max_int-1
        if num < 0 and min_int > num:
            return min_int
        if max_int < num:
            return max_int
        return num        

    def isSymbol(self, s):
        if s == '-' or s == '+':
            return True
        else:
            return False

    def number(self, s):
        if s == '0':
            return 0
        elif s == '1':
            return 1
        elif s == '2':
            return 2
        elif s == '3':
            return 3
        elif s == '4':
            return 4
        elif s == '5':
            return 5
        elif s == '6':
            return 6
        elif s == '7':
            return 7
        elif s == '8':
            return 8
        elif s == '9':
            return 9
        else:
            return None

if __name__ == "__main__":
    test = Solution()
    result = test.myAtoi('        -12a')
    print result, result == 0