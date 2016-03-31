"""
5. Longest Palindromic Substring

Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, 
and there exists one unique longest palindromic substring.

"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ''
        longest_length = 0
        for start_index, char in enumerate(s):
            end_index = s.rfind(char, start_index, len(s))
            while end_index != -1:
                substring = s[start_index:end_index+1]
                if longest_length >= len(substring):
                    break
                if self.isPalindrome(substring) and longest_length < len(substring):
                    longest = substring
                    longest_length = len(substring)
                end_index = s.rfind(char, start_index, end_index)
        return longest
    
    def isPalindrome(self, s):
        return s == s[::-1]

if __name__ == "__main__":
    test = Solution()
    print test.longestPalindrome("a")