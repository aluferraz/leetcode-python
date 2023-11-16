import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        indexes = collections.defaultdict(list)
        N = len(s)
        ans = 0
        for i in range(N):
            indexes[s[i]].append(i)
        used = [[False for _ in range(26)] for _ in range(26)]

        for i in range(1, N - 1):
            c = s[i]
            for j in range(26):
                boundary = chr(ord('a') + j)
                if used[ord(c) - ord('a')][ord(boundary) - ord('a')]:
                    continue
                if boundary in indexes:
                    has_left = indexes[boundary][0] < i
                    has_right = indexes[boundary][-1] > i
                    if has_left and has_right:
                        used[ord(c) - ord('a')][ord(boundary) - ord('a')] = True
                        ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class UniqueLength3PalindromicSubsequences(Solution):
    pass
