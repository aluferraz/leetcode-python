import collections
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumScore(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        N = len(s)
        M = len(t)

        prefix = [N] * M
        suffix = [-1] * M

        def fill_reach(arr, sstr, tstr):
            i = 0
            for j in range(M):
                target = tstr[j]
                pos = sstr.find(target, i)
                if pos == -1:
                    pos = N
                arr[j] = pos
                i = pos + 1

        def fill_reach_back(arr, sstr, tstr):
            j = M - 1
            for i in range(N - 1, -1, -1):
                if sstr[i] == tstr[j]:
                    arr[j] = i
                    j -= 1
                if j < 0:
                    break

        fill_reach(prefix, s, t)
        fill_reach_back(suffix, s, t)

        best = M
        INF = 10 ** 20
        for i in range(M):
            closest_suffix = INF
            for j in range(M - 1, i + 1, -1):
                if suffix[j] > prefix[i]:
                    closest_suffix = j
                else:
                    break
            use_prefix = closest_suffix - i - 1
            if prefix[i] < N:
                best = min(best, M - i - 1)
            best = min(use_prefix, best)
        for j in range(M - 1, -1, -1):
            if suffix[j] == -1:
                continue
            best = min(best, j)
        return best

        # leetcode submit region end(Prohibit modification and deletion)


class SubsequenceWithTheMinimumScore(Solution):
    pass
