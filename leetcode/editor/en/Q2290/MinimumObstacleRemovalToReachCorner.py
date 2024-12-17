import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        q = collections.deque([(0, 0, grid[0][0])])
        ans = N * M

        def is_valid_idx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M

        visited = [[(N * M) for _ in range(M)] for _ in range(N)]
        visited[0][0] = grid[0][0]

        DIRECTIONS = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]
        while q:
            size = len(q)
            for _ in range(size):
                i, j, walls = q.popleft()
                visited[i][j] = walls
                for di, dj in DIRECTIONS:
                    ni, nj = i + di, j + dj
                    if is_valid_idx(ni, nj):
                        cost = walls + grid[ni][nj]
                        if (ni, nj) == (N - 1, M - 1):
                            ans = min(ans, cost)
                        elif cost < visited[ni][nj]:
                            q.append((ni, nj, cost))
                            visited[ni][nj] = cost
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumObstacleRemovalToReachCorner(Solution):
    pass
