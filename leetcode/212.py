"""
212. World Search II
 
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" 
cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

For example, Given 
words = ["oath","pea","eat","rain"] and 

board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
  ]

Return ["eat","oath"].

Note:
You may assume that all inputs are consist of lowercase letters a-z. 


Hint: 
You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. 
What kind of data structure could answer such query efficiently? Does a hash table work? 
Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, 
please work on this problem: Implement Trie (Prefix Tree) first.

"""
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(board) == 0:
            return []
        trie = self.createTrie(words)
        self.visited = [[False for x in range(len(board[y]))] for y in range(len(board))]
        self.result = set([])
        for row in range(len(board)):
            for col in range(len(board[row])):
                self.find_helper(row, col, board, '', trie)
        return sorted(list(self.result))

    def find_helper(self, row, col, board, prefix, t):
        if '#' in t:
            self.result.add(prefix)
        if (0 <= row < len(board) and 0 <= col < len(board[row]) and
            board[row][col] in t and not self.visited[row][col]):
                char = board[row][col]
                self.visited[row][col] = True
                self.find_helper(row-1, col, board, prefix+char, t[char])
                self.find_helper(row+1, col, board, prefix+char, t[char])
                self.find_helper(row, col-1, board, prefix+char, t[char])
                self.find_helper(row, col+1, board, prefix+char, t[char])
                self.visited[row][col] = False

    def createTrie(self, words):
        trie = {}
        t = trie
        for word in words:
            for c in word:
                if not c in t:
                    t[c] = {}
                t = t[c]
            t['#'] = {}
            t = trie
        return trie

if __name__ == "__main__":
    test = Solution()
    words = ["oath","pea","eat","rain"]
    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    result = test.findWords(board,words)
    # Should print ["eat","oath"]
    print result
    board = ["aa"]
    words = ["a"]
    result = test.findWords(board, words)
    print result
    board = ["aaaa","aaaa","aaaa"]
    words = ["aaaaaaaaaaaa","aaaaaaaaaaaaa","aaaaaaaaaaab"]
    result = test.findWords(board, words)
    print result
    # words = ["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"]
    # board = ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa",
    #          "bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa",
    #          "babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa",
    #          "aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab",
    #          "aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa",
    #          "aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb",
    #          "aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab",
    #          "bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab",
    #          "aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa",
    #          "abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
    # result = test.findWords(board,words)
    # print result
    # result = test.findWords([], [])
    # print result