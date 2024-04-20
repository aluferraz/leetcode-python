from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findFarmland(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        M = len(grid[0])

        def is_valid_idx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M and grid[i][j] == 1

        def explore(i, j):
            DIRECTIONS = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]
            bottom_right = (i, j)
            for di, dj in DIRECTIONS:
                if is_valid_idx(i + di, j + dj):
                    grid[i + di][j + dj] = 2
                    bottom_right = max(bottom_right, explore(i + di, j + dj))
            return bottom_right

        ans = []
        for i in range(N):
            for j in range(M):
                if is_valid_idx(i, j):
                    ans_here = [(i, j), explore(i, j)]
                    ans.append([ans_here[0][0],
                                ans_here[0][1],
                                ans_here[1][0],
                                ans_here[1][1]])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class FindAllGroupsOfFarmland(Solution):
    pass
