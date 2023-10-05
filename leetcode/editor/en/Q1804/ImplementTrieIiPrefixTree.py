import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)

class TrieNode:

    def __init__(self, key, isEnding, words):
        self.key = key
        self.children = collections.defaultdict(int)
        self.c_counter = collections.defaultdict(int)
        self.isEnding = isEnding
        self.words = words


class Trie(object):

    def __init__(self):
        self.root = TrieNode("", False, collections.defaultdict(int))

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for c in word:
            if not (c in current.children):
                w = collections.defaultdict(int)
                current.children[c] = TrieNode(c, False, w)
            current.words[word] += 1
            current.c_counter[c] += 1
            current = current.children[c]
        current.words[word] += 1
        current.c_counter[word[-1]] += 1
        current.isEnding = True

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        return self.root.words[word]

    def countWordsStartingWith(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        current = self.root
        for c in prefix:
            if not (c in current.children):
                return 0
            current = current.children[c]
        return sum(current.words.values())

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for c in word:
            if not (c in current.children):
                return
            current.words[word] -= 1
            current.c_counter[c] -= 1
            current = current.children[c]

        current.words[word] -= 1
        current.c_counter[word[-1]] -= 1
        current = self.root
        for c in word:
            if not (c in current.children):
                return
            if current.words[word] == 0:
                current.words.pop(word)
            if current.c_counter[c] == 0:
                current.c_counter.pop(c)
                return
            current = current.children[c]

    # Your Trie object will be instantiated and called as such:


# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
# leetcode submit region end(Prohibit modification and deletion)


class ImplementTrieIiPrefixTree(Trie):
    pass
