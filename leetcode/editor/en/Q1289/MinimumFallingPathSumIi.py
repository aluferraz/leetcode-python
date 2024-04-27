from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        N = len(grid)
        M = len(grid[0])
        INF = 10 ** 20
        cache = list(grid[0])
        for i in range(1, N):
            min_seen = INF
            row = list(grid[i])
            for j in range(M):
                grid[i][j] = row[j] + min_seen
                min_seen = min(min_seen, cache[j])
            min_seen = INF
            for j in range(M - 1, -1, -1):
                grid[i][j] = min(row[j] + min_seen, grid[i][j])
                min_seen = min(min_seen, cache[j])
            cache = list(grid[i])
        return min(grid[-1])

        #
        # N = len(grid)
        # M = len(grid[0])
        # INF = 10 ** 20
        #
        # cache = [[-1 for _ in range(M + 1)] for _ in range(N)]
        # has_cache = [[False for _ in range(M + 1)] for _ in range(N)]
        #
        # def go(row, pcol):
        #     if row == N:
        #         return 0
        #     if has_cache[row][pcol]:
        #         return cache[row][pcol]
        #     ans = INF
        #     for j in range(M):
        #         if j == pcol:
        #             continue
        #         ans = min(ans, grid[row][j] + go(row + 1, j))
        #     cache[row][pcol] = ans
        #     has_cache[row][pcol] = True
        #     return ans
        #
        # return go(0, M)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumFallingPathSumIi(Solution):
    pass
