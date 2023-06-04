# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        N = len(grid)
        M = len(grid[0])
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        def isValidIdx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M

        cache = {}
        MOD = (10 ** 9) + 7

        def count(row, col):
            if (row, col) in cache:
                return cache[(row, col)]
            ans = 0
            for yi, xi in directions:
                newRow = row + yi
                newCol = col + xi
                if isValidIdx(newRow, newCol) and grid[newRow][newCol] > grid[row][col]:
                    ans = ((ans + 1) % MOD) + (count(newRow, newCol) % MOD)
            ans %= MOD
            cache[(row, col)] = ans
            return ans

        ans = (N * M) % MOD
        for i in range(N):
            for j in range(M):
                ans = (ans + count(i, j)) % MOD

        return ans

    # leetcode submit region end(Prohibit modification and deletion)


class NumberOfIncreasingPathsInAGrid(Solution):
    pass
