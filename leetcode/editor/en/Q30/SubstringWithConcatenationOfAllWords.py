import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ans = []
        N = len(s)
        M = len(words)
        words_len = 0
        w_map = collections.defaultdict(int)
        for w in words:
            words_len += len(w)
            w_map[w] += 1
        sw_len = len(words[0])
        left = 0
        right = words_len
        window_mask = collections.deque()
        while right <= N:
            while left < right:
                prefix = s[left:left + sw_len]
                if prefix in w_map and w_map[prefix] > 0:
                    window_mask.append(prefix)
                    w_map[prefix] -= 1
                    left += sw_len
                else:
                    break
            if left == right:
                ans.append(right - words_len)
            while len(window_mask) > 0:
                w_map[window_mask.popleft()] += 1
            right += 1
            left = right - words_len

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SubstringWithConcatenationOfAllWords(Solution):
    pass
