"""
208. Implement Trie (Prefix Tree)
 
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z. 

"""
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.chars = {}

    def __str__(self):
        string = ''
        for c in self.chars:
            string += '{} - {}'.format(c, self.chars[c])
        return string

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def __str__(self):
        return str(self.root)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        t = self.root
        for c in word:
            if not c in t.chars:
                t.chars[c] = TrieNode()
            t = t.chars[c]
        t.chars['#'] = TrieNode()

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        t = self.root
        for c in word:
            if not c in t.chars:
                return False
            t = t.chars[c]
        if '#' in t.chars:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        t = self.root
        for c in prefix:
            if not c in t.chars:
                return False
            t = t.chars[c]
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

if __name__ == "__main__":
    test = Trie()
    test.insert("oath")
    test.insert("pea")
    print test
    print test.search('oath')
    print test.search('pea')
    print test.search('oat')
    print test.startsWith('oat')
    print test.startsWith('ot')
    # words = ["oath","pea","eat","rain"]
    # board = [
    #   ['o','a','a','n'],
    #   ['e','t','a','e'],
    #   ['i','h','k','r'],
    #   ['i','f','l','v']
    # ]
    # result = test.findWords(board,words)
    # Should print ["eat","oath"]
    # print result
