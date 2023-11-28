from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def knightDialer(self, N):
        """
        :type n: int
        :rtype: int
        """

        jumps = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        MOD = 10 ** 9 + 7
        cache = [[0 for _ in range(N + 1)] for _ in range(10)]
        has_cache = [[False for _ in range(N + 1)] for _ in range(10)]

        def go(i, k):
            if k == 0:
                return 1
            if has_cache[i][k]:
                return cache[i][k]
            ans = 0
            for x in jumps[i]:
                ans = (ans + go(x, k - 1)) % MOD
            has_cache[i][k] = True
            cache[i][k] = ans
            return ans

        ans = 0

        for i in range(10):
            ans = (ans + go(i, N - 1)) % MOD
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class KnightDialer(Solution):
    pass
