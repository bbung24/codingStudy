"""
12. Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "nulla"
        mapping = { 1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 
            90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        output = ""
        for div in sorted(mapping.keys(), reverse=True):
            multiplier = num / div
            num = num % div
            output += multiplier * mapping[div]
        return output


if __name__ == "__main__":
    test = Solution()
    # Should print nulla
    result = test.intToRoman(0)
    print result
    # Should print I
    result = test.intToRoman(1)
    print result
    # Should print IV
    result = test.intToRoman(4)
    print result
    # Should print VI
    result = test.intToRoman(6)
    print result
    # Should print XL
    result = test.intToRoman(40)
    print result
    # Should print CD
    result = test.intToRoman(400)
    print result
    # Should print MMMCMXCIX
    result = test.intToRoman(3999)
    print result