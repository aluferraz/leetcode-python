from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])

        def is_valid_idx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M and grid[i][j] == "1"

        def explore(i, j):
            DIRECTIONS = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]
            for di, dj in DIRECTIONS:
                if is_valid_idx(i + di, j + dj):
                    grid[i + di][j + dj] = "2"
                    explore(i + di, j + dj)

        ans = 0
        for i in range(N):
            for j in range(M):
                if is_valid_idx(i, j):
                    ans += 1
                    explore(i, j)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfIslands(Solution):
    pass
