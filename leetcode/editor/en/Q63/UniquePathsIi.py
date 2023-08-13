import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if obstacleGrid[0][0] == 1:
            return 0
        N = len(obstacleGrid)
        M = len(obstacleGrid[0])

        DIRECTIONS = [
            (1, 0),
            (0, 1)
        ]

        # def coords_to_number(i, j):
        #     return (i * M) + j

        def is_valid_idx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M and obstacleGrid[i][j] != 1

        counter_grid = [[0 for _ in range(M)] for _ in range(N)]

        def bfs():
            q = collections.deque()

            q.append((0, 0))
            counter_grid[0][0] += 1

            while len(q) > 0:
                size = len(q)
                for _ in range(size):
                    i, j = q.popleft()

                    for y, x in DIRECTIONS:
                        newI = i + y
                        newJ = j + x
                        if is_valid_idx(newI, newJ):
                            if counter_grid[newI][newJ] == 0:
                                q.append((newI, newJ))
                            counter_grid[newI][newJ] += counter_grid[i][j]

        bfs()

        return counter_grid[N - 1][M - 1]

    # leetcode submit region end(Prohibit modification and deletion)


class UniquePathsIi(Solution):
    pass
