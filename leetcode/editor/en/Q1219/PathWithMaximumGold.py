from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = 0
        N = len(grid)
        M = len(grid[0])

        def is_valid_idx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M and grid[i][j] > 0

        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        def get_gold(i, j):
            ans_here = grid[i][j]
            grid[i][j] = 0
            best_path = 0
            for dy, dx in DIRECTIONS:
                if is_valid_idx(i + dy, j + dx):
                    best_path = max(best_path, get_gold(i + dy, j + dx))
            grid[i][j] = ans_here
            ans_here += best_path
            return ans_here

        for i in range(N):
            for j in range(M):
                if is_valid_idx(i, j):
                    ans = max(ans, get_gold(i, j))

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class PathWithMaximumGold(Solution):
    pass
