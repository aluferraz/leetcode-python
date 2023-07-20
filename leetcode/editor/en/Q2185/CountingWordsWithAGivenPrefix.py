from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        ans = 0
        N = len(pref)
        for w in words:
            if len(w) < N:
                continue
            if w[:N] == pref:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class CountingWordsWithAGivenPrefix(Solution):
    pass
