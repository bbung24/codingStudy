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
"""
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(board) == 0 or len(board[0]) == 0 or len(words) == 0:
          return []
        first_letters = set([x[0] for x in words])
        row_length = len(board)
        col_length = len(board[0])
        max_word_length = max([len(x) for x in words])
        result = set([])
        for row in range(row_length):
          for col in range(col_length):
            if board[row][col] in first_letters:
              visited = set([])
              visited.add((row,col))
              word = ''
              copy_words = [x for x in words]
              self.find_helper(row, col, word, board, copy_words, visited, result, max_word_length)
        return sorted(result)

    def find_helper(self, row, col, word, board, words, visited, result, max_word_length):
        """
        :type row: int
        :type col: int
        :type word: string
        :type board: List[List[str]]
        :type words: List[str]
        :type visited: List[tuple]
        """
        word += board[row][col]
        self.check_word_exists(word, words, result)
        if len(result) != len(words) and len(word) <= max_word_length:
          if row-1 >= 0 and (row-1, col) not in visited:
            copy_word = word
            copy_visited = set([x for x in visited])
            copy_visited.add((row-1, col))
            self.find_helper(row-1, col, copy_word, board, words, copy_visited, result, max_word_length)
          if col-1 >= 0 and (row, col-1) not in visited:
            copy_word = word
            copy_visited = set([x for x in visited])
            copy_visited.add((row, col-1))
            self.find_helper(row, col-1, copy_word, board, words, copy_visited, result, max_word_length)
          if row+1 < len(board) and (row+1, col) not in visited:
            copy_word = word
            copy_visited = set([x for x in visited])
            copy_visited.add((row+1, col))
            self.find_helper(row+1, col, copy_word, board, words, copy_visited, result, max_word_length)
          if col+1 < len(board[0]) and (row, col+1) not in visited:
            copy_word = word
            copy_visited = set([x for x in visited])
            copy_visited.add((row, col+1))
            self.find_helper(row, col+1, copy_word, board, words, copy_visited, result, max_word_length)

    def check_word_exists(self, word, words, result):
        """
        :type word: string
        :type words: List[str]
        """
        for w in words:
          if w == word:
            result.add(word)

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
    words = ["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"]
    board = ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
    result = test.findWords(board,words)
    print result
    result = test.findWords([], [])
    print result