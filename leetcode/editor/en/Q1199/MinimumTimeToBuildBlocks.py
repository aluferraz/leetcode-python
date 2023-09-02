import sys
from functools import cache
from typing import List

sys.setrecursionlimit(5000)


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minBuildTime(self, blocks, split):
        """
        :type blocks: List[int]
        :type split: int
        :rtype: int
        """

        blocks.sort(reverse=True)
        N = len(blocks)
        INF = 10 ** 20
        if N == 1:
            return blocks[0]
        dp = [
            [INF] * (N + 1) for _ in range(N + 1)
        ]

        for w in range(N + 1):
            dp[N][w] = 0  # I completed the N tasks

        for i in range(N - 1, -1, -1):
            for w in range(N, 0, -1):
                dp[i][w] = max(blocks[i], dp[i + 1][w - 1])
                dp[i][w] = min(dp[i][w], (split + dp[i][min(w * 2, (N - i))]))
        return dp[0][1]
        #
        # cache = {}
        #
        # def solve(w, i):
        #     if w == 0:
        #         return INF
        #     if i == -1:
        #         return 0
        #     if w >= (i + 1):
        #         return blocks[i]
        #     if (w, i) in cache:
        #         return cache[(w, i)]
        #     split_and_build = split + solve(w * 2, i)
        #     build_and_split = INF
        #     if w > 1:
        #         build_and_split = max(blocks[i], solve((w - 1), i - 1))
        #     ans = min(split_and_build, build_and_split)
        #     cache[(w, i)] = ans
        #     return ans
        #
        # return solve(1, N - 1)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumTimeToBuildBlocks(Solution):
    pass
