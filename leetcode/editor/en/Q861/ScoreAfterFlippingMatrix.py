from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        for i in range(N):
            if grid[i][0] == 0:
                for j in range(M):
                    grid[i][j] = (grid[i][j] + 1) % 2
        cols = [0] * M
        for j in range(M):
            for i in range(N):
                cols[j] += grid[i][j]
        for j in range(M):
            if cols[j] < (N // 2):
                for i in range(N):
                    grid[i][j] = N - cols[j]

        ans = 0
        for j in range(M):
            ans *= 2
            ans += cols[j]

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class ScoreAfterFlippingMatrix(Solution):
    pass
