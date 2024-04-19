from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        ans = 0
        N = len(grid)
        M = len(grid[0])
        DIRECTIONS = [
            (1,0),
            (-1,0),
            (0,-1),
            (0, 1)
        ]

        def isValidIdx(i,j):
            return i >= 0 and i < N and j >= 0 and j < M

        def count(i,j):
            ans_here = 0
            for di, dj in DIRECTIONS:
                if not isValidIdx(i+di, j+dj) and grid[i+di][j+dj] == 0:
                    ans_here += 1
            return ans_here


        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    ans += count(i,j)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


class IslandPerimeter(Solution):
    pass