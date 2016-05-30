"""
65. Valid Number

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. 
You should gather all requirements up front before implementing one.

"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sign = False
        dot = False
        prevNum = False
        nextNum = False
        e = False
        s = s.strip()
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        if len(s) == 0:
            return False
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        if len(s) == 0:
            return False
        prevChar = ''
        for char in s:
            if char == '.' and not dot and not e:
                dot = True
            elif char == 'e' and not e and prevNum:
                e = True
            elif (char == '-' or char == '+') and prevChar =='e':
                sign = True
            elif char in numbers:
                if not prevNum:
                    prevNum = True
                elif not nextNum and e:
                    nextNum = True
            else:
                return False
            prevChar = char
        if not e and prevNum:
            return True
        else:
            if prevNum and nextNum:
                return True
            else:
                return False
        
if __name__ == "__main__":
    test = Solution()
    # Should print True
    print test.isNumber('0')
    # Should print False
    print test.isNumber('-')
    # Should print True
    print test.isNumber(' 0.1')
    # Should print True
    print test.isNumber('.1')
    # Should print True
    print test.isNumber('2e10')
    # Should print True
    print test.isNumber('+100')
    # Should print True
    print test.isNumber('-1')
    # Should print False
    print test.isNumber('abc')
    # Should print False
    print test.isNumber('1 a')
    # Should print False
    print test.isNumber('10+100')
    # Should print False
    print test.isNumber('')
    # Should print False
    print test.isNumber('12e')
    # Should print False
    print test.isNumber('1012e10.0')
    # Should print False
    print test.isNumber(".")
    # Should print True
    print test.isNumber(" 005047e+6")
    # Should print False
    print test.isNumber("3-2")