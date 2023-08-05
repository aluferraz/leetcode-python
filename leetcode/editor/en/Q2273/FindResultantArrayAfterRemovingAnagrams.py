import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        N = len(words)
        words.reverse()
        ans = collections.deque()
        words_sorted = list(words)
        for i in range(N):
            w = list(words_sorted[i])
            w.sort()
            words_sorted[i] = w

        for i in range(N):
            if i > 0:
                if words_sorted[i - 1] == words_sorted[i]:
                    ans.pop()
            ans.append(words[i])
        ans.reverse()
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class FindResultantArrayAfterRemovingAnagrams(Solution):
    pass
