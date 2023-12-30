# leetcode submit region begin(Prohibit modification and deletion)
import math

from functools import cache
from typing import List


class Solution(object):
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        N = len(jobDifficulty)
        if d > N:
            return -1
        INF = 10 ** 20
        boundary = max(int(math.ceil(math.log2(N))), 1)
        RMQS = [[-INF for _ in range(boundary)] for _ in range(N)]

        def preprocessing():
            for i in range(N):
                RMQS[i][0] = jobDifficulty[i]
            # sparse table

            for j in range(1, boundary):
                i = 0
                while (i + (1 << j) - 1) < N:
                    RMQS[i][j] = max(RMQS[i][j - 1], RMQS[i + (1 << (j - 1))][j - 1])
                    i += 1

        preprocessing()

        def int_log2(x):
            k = 0
            while (1 << (k + 1)) <= x:
                k += 1
            return k

        def cost(l, r):
            rlen = r - l + 1
            k = int_log2(rlen)
            second_range_begin = (r - (1 << k)) + 1
            max_here = max(RMQS[l][k], RMQS[second_range_begin][k])
            return max_here

        cache = [[INF for _ in range(d + 1)] for _ in range(N)]
        has_cache = [[False for _ in range(d + 1)] for _ in range(N)]

        def go(l, k):
            if l == N:
                return 0
            if k == 1:
                return cost(l, N - 1)
            if has_cache[l][k]:
                return cache[l][k]
            r = N - k + 1
            ans = INF
            for i in range(l, r):
                left_cost = cost(l, i)
                remaining_cost = go(i + 1, k - 1)
                ans_here = left_cost + remaining_cost
                ans = min(ans, ans_here)
            cache[l][k] = ans
            has_cache[l][k] = True
            return ans

        ans = go(0, d)
        return ans

    # def minDifficulty(self, jobDifficulty, d):
    #     """
    #     :type jobDifficulty: List[int]
    #     :type d: int
    #     :rtype: int
    #     """
    #     if (d > len(jobDifficulty)):
    #         return -1
    # 
    #     hasCache = [[False for _ in range(0, len(jobDifficulty))] for i in range(0, d + 1)]
    #     cache = [[False for _ in range(0, len(jobDifficulty))] for i in range(0, d + 1)]
    # 
    #     def solve(i, d):
    #         if i >= len(jobDifficulty):
    #             return 0
    #         if d == 0:
    #             return 0
    #         if hasCache[d][i]:
    #             return cache[d][i]
    # 
    #         boundary = len(jobDifficulty) - d + 1
    #         jobCost = -1
    #         best = 100000000000
    # 
    #         for j in range(i, boundary):
    #             jobCost = max(jobCost, jobDifficulty[j])
    #             if d == 1:
    #                 best = jobCost
    #             else:
    #                 ansHere = jobCost + solve(j + 1, d - 1)
    #                 best = min(best, ansHere)
    # 
    #         cache[d][i] = best
    #         hasCache[d][i] = True
    #         return best
    # 
    #     return solve(0, d)


class MinimumDifficultyOfAJobSchedule(Solution):
    pass
# leetcode submit region end(Prohibit modification and deletion)
