import sys

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        sys.setrecursionlimit(10 ** 7)
        MOD = 10 ** 9 + 7
        N = len(corridor)
        # psum = [0] * (N + 1)
        # for i in range(1, N + 1):
        #     psum[i] = psum[i - 1] + (1 if corridor[i - 1] == 'S' else 0)
        cache = [[0 for _ in range(3)] for _ in range(N + 1)]
        has_cache = [[False for _ in range(3)] for _ in range(N + 1)]

        def go(i, seats):
            if i == N:
                return 1 if seats == 2 else 0
            if has_cache[i][seats]:
                return cache[i][seats]
            ans = 0
            seats += (1 if corridor[i] == 'S' else 0)
            if seats > 2:
                return 0
            if seats == 2:
                # can split
                ans += go(i + 1, 0)
            ans += go(i + 1, seats)
            has_cache[i][seats] = True
            cache[i][seats] = ans
            return ans

        ans = go(0, 0)
        return ans % MOD


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfWaysToDivideALongCorridor(Solution):
    pass
