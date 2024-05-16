import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        if grid[0][0] == 1:
            return 0

        queue = collections.deque()

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    grid[i][j] = -1
                else:
                    grid[i][j] = 10 ** 4

        def is_valid_idx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M and grid[i][j] >= 0

        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                i, j, d = queue.popleft()
                for dy, dx in DIRECTIONS:
                    if is_valid_idx(i + dy, j + dx) and grid[i + dy][j + dx] > d + 1:
                        grid[i + dy][j + dx] = d + 1
                        queue.append((i + dy, j + dx, d + 1))

        queue.append((0, 0))
        path = [[0 for _ in range(M)] for _ in range(N)]
        path[0][0] = grid[0][0]
        enqueued = collections.defaultdict(int)
        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                d = path[i][j]
                if i == N - 1 and j == M - 1:
                    continue
                for dy, dx in DIRECTIONS:
                    if is_valid_idx(i + dy, j + dx) and d > path[i + dy][j + dx]:
                        path[i + dy][j + dx] = min(d, grid[i + dy][j + dx])
                        if enqueued[(i + dy, j + dx)] < path[i + dy][j + dx]:
                            enqueued[(i + dy, j + dx)] = path[i + dy][j + dx]
                            queue.append((i + dy, j + dx))
        return path[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)


class FindTheSafestPathInAGrid(Solution):
    pass
