from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        INF = 10 ** 20
        N = len(s1)
        M = len(s2)

        cache = [
            [None for _ in range(M + 1)] for _ in range(N + 1)
        ]

        def go(i, j):
            if i == N and j == M:
                return 0
            if i == N and j < M:
                ans = ord(s2[j]) + go(i, j + 1)
                cache[i][j] = ans
                return cache[i][j]
            if j == M and i < N:
                ans = ord(s1[i]) + go(i + 1, j)
                cache[i][j] = ans
                return cache[i][j]
            if cache[i][j] is not None:
                return cache[i][j]
            ans = INF
            if s1[i] == s2[j]:
                ans = min(ans, go(i + 1, j + 1))
            ans = min(ans, ord(s1[i]) + go(i + 1, j))
            ans = min(ans, ord(s2[j]) + go(i, j + 1))
            cache[i][j] = ans
            return ans

        return go(0, 0)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumAsciiDeleteSumForTwoStrings(Solution):
    pass
