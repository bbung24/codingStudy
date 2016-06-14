"""
126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, 
find all shortest transformation sequence(s) from beginWord to endWord, such that:

1. Only one letter can be changed at a time
2. Each intermediate word must exist in the word list

For example,

Given:
beginWord = "hit"
endWord = "cog"
wordlist = ["hot", "dot", "dog", "lot", "log"]

Return
[
    ["hit", "hot", "dot", "dog", "cog"],
    ["hit", "hot", "lot", "log", "cog"]
]

Note:
    All words have the same length.
    All words contain only lowercase alphabetic characters.

"""
class Node(object):
    def __init__(self, text):
        self.text = text
        self.visited = False
        self.neighbors = []

    def _is_valid_operand(self, other):
        return hasattr(other, "text")
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.text == other.text
    def __str__(self):
        return '{}:{}'.format(self.text, self.neighbors)

class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[string]]
        """
        if beginWord == '' or endWord == '' or len(wordlist) == 0:
            return []
        self.path_weight = {}
        self.previous = {}
        self.remaining = []
        wordlist.add(beginWord)
        wordlist.add(endWord)
        self.createGraph(wordlist)
        startNode = self.initializeNode(beginWord)
        endNode = self.initializeNode(endWord)
        for node in self.graph:
            self.remaining.append(node)
            self.path_weight[node] = float('inf')
        self.path_weight[startNode] = 0
        self.previous[startNode] = None
        while len(self.remaining) > 0:
            node = self.findMinNode()
            if node == None:
                # No Solution
                return []
            for adj in node.neighbors:
                next_dist = self.path_weight[node] + 1
                if next_dist < self.path_weight[adj]:
                    self.path_weight[adj] = next_dist
                    self.previous[adj] = node
        self.result = []
        # for n in self.path_weight:
        #     print n.text, self.path_weight[n]
        self.buildRoute(endNode)
        return self.result

    def buildRoute(self, prev):
        if prev != None:
            self.result.append(prev.text)
            self.buildRoute(self.previous[prev])
        else:
            self.result.reverse()
        
    def findMinNode(self):
        minimum_weight = float('inf')
        minimum_node = None
        for node in self.remaining:
            pw = self.path_weight[node]
            if pw < minimum_weight:
                minimum_weight = pw
                minimum_node = node
        if minimum_node == None:
            return None
        return self.remaining.pop(self.remaining.index(minimum_node))
            
    def initializeNode(self, word):
        node = Node(word)
        if node in self.graph:
            node = self.graph[self.graph.index(node)]
        else:
            self.graph.append(node)
        return node

    def initializeRelationship(self, node):
        for n1 in self.graph:
            if n1 != node and self.isNeighbor(node.text, n1.text):
                node.neighbors.append(n1)

    def createGraph(self, wordlist):
        self.graph = []
        for word in wordlist:
            self.initializeNode(word)
        for node in self.graph:
            self.initializeRelationship(node)

    def isNeighbor(self, w1, w2):
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
        if diff > 1:
            return False
        else:
            return True
        
if __name__ == "__main__":
    test = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordlist = set(["hot", "dot", "dog", "lot", "log"])
    # Should print [
    #     ["hit", "hot", "dot", "dog", "cog"],
    #     ["hit", "hot", "lot", "log", "cog"]
    # ]
    print test.findLadders(beginWord, endWord, wordlist)
    beginWord = "hit"
    endWord = "cog"
    wordlist = set(["hot", "dot","lot"])
    # Should print [
    #     ["hit", "hot", "dot", "dog", "cog"],
    #     ["hit", "hot", "lot", "log", "cog"]
    # ]
    print test.findLadders(beginWord, endWord, wordlist)
    beginWord = "qa"
    endWord = "sq"
    wordlist = set(["si","go","se","cm","so","ph","mt","db",
        "mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca",
        "br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr",
        "po","fe","ho","ma","re","or","rn","au","ur","rh","sr",
        "tc","lt","lo","as","fr","nb","yb","if","pb","ge","th",
        "pm","rb","sh","co","ga","li","ha","hz","no","bi","di",
        "hi","qa","pi","os","uh","wm","an","me","mo","na","la",
        "st","er","sc","ne","mn","mi","am","ex","pt","io","be",
        "fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])
    # Should print [
    #     ["a", "b", "c"]
    # ]
    print test.findLadders(beginWord, endWord, wordlist)