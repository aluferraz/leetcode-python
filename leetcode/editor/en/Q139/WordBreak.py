import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        trieObj = Trie()
        for w in wordDict:
            trieObj.from_str(w)
        N = len(s)

        cache = {}

        def go(current, i):
            if i == N:
                return trieObj.ending_char in current
            if (current['wid'], i) in cache:
                return cache[(current['wid'], i)]
            char = s[i]
            ans = False
            if char in current:
                ans = ans or go(current[char], i + 1)
            if trieObj.ending_char in current and char in trieObj.trie:
                ans = ans or go(trieObj.trie[char], i + 1)
            cache[(current['wid'], i)] = ans
            return ans

        return go(trieObj.trie, 0)


class Trie:

    def __init__(self, s=""):
        self.trie = {
            'wid': ''
        }
        self.ending_char = '*'
        if len(s) > 0:
            self.from_str(s)
        self.wids = set()

    def from_str(self, s):
        current = self.trie
        prev_wid = ""
        for char in s:
            if char not in current:
                # if prev_wid + char in self.wids:
                #     print("a")
                current[char] = {
                    'wid': prev_wid + char
                }
            current = current[char]
            prev_wid = current['wid']
            # self.wids.add(current['wid'])

        current[self.ending_char] = True
        current['wid'] = current['wid'] + self.ending_char

    # leetcode submit region end(Prohibit modification and deletion)


class WordBreak(Solution):
    pass
