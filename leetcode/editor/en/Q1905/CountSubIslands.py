from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        N = len(grid1)
        M = len(grid1[0])
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),

        ]

        def is_valid_idx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M

        def go(i, j):
            if not is_valid_idx(i, j):
                return
            if grid2[i][j] != 1:
                return
            grid2[i][j] = 2
            for di, dj in DIRECTIONS:
                go(i + di, j + dj)
            return

        def go2(i, j):
            if not is_valid_idx(i, j):
                return True
            if grid2[i][j] != 2:
                return True
            is_fully_covered = True
            if grid2[i][j] == 2 and grid1[i][j] == 0:
                is_fully_covered = False
            grid2[i][j] = 3
            for di, dj in DIRECTIONS:
                valid_here = go2(i + di, j + dj)
                is_fully_covered = is_fully_covered and valid_here
            return is_fully_covered

        islands = 0
        for i in range(N):
            for j in range(M):
                if grid2[i][j] == 1:
                    go(i, j)

        for i in range(N):
            for j in range(M):
                if grid2[i][j] == 2:
                    if go2(i, j):
                        islands += 1

        return islands


# leetcode submit region end(Prohibit modification and deletion)


class CountSubIslands(Solution):
    pass
