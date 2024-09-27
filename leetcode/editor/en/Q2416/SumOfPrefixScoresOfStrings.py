from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        class TrieNode:
            def __init__(self, score=0):
                self.score = score
                self.children = {}

        trie = TrieNode()

        def add(s, root):
            current = root
            for c in s:
                if c not in current.children:
                    current.children[c] = TrieNode()
                current = current.children[c]
                current.score += 1

            current.children['*'] = TrieNode()

        N = len(words)
        ans = [0] * N

        for i in range(N):
            M, w, real_idx = (len(words[i]), words[i], i)
            add(w, trie)
        for i in range(N):
            node = trie
            score_here = 0
            for c in words[i]:
                node = node.children[c]
                score_here += node.score
            ans[i] = score_here

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SumOfPrefixScoresOfStrings(Solution):
    pass
