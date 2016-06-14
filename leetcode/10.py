"""
10. Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
if __name__ == "__main__":
    test = Solution()
    result = test.isMatch("aa","a")
    print result == False
    result = test.isMatch("aa","aa")
    print result == True
    result = test.isMatch("aaa","aa")
    print result == False
    result = test.isMatch("aa", "a*")
    print result == True
    result = test.isMatch("aa", ".*")
    print result == True
    result = test.isMatch("ab", ".*")
    print result == True
    result = test.isMatch("aab", "c*a*b")
    print result == True