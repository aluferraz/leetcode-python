from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordTrie = {"": {}}

        def buildTrie(s, trie):
            cur = trie
            for c in s:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['*'] = s

        for w in wordDict:
            buildTrie(w, wordTrie[""])
        N = len(s)
        ans = []

        def go(i, curTrie, curWords):
            c = s[i]
            if c not in curTrie:
                return
            curTrie = curTrie[c]
            if i == N - 1:
                if '*' in curTrie:
                    curWords.append(curTrie['*'])
                    ans.append(" ".join(curWords))
                    curWords.pop()
                return

            if '*' in curTrie:
                curWords.append(curTrie['*'])
                # go(i, wordTrie[""], curWords)  # Start with the same letter
                go(i + 1, wordTrie[""], curWords)  # Start with the next letter
                curWords.pop()
            return go(i + 1, curTrie, curWords)

        go(0, wordTrie[""], [])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class WordBreakIi(Solution):
    pass
