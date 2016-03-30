"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = set()
        max_length = 0
        for index in range(len(s)):
            if max_length > len(s[index:]):
                break
            for letter in s[index:]:
                if letter not in letters:
                    letters.add(letter)
                else:
                    max_length = max(max_length, len(letters))
                    letters.clear()
                    break
        return max(max_length, len(letters))

if __name__ == "__main__":
    test = Solution()
    print test.lengthOfLongestSubstring('dvdf')