import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        DIRECTIONS = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        N = len(maze)
        M = len(maze[0])

        def isValidIdx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M and maze[i][j] == 0

        if not isValidIdx(start[0], start[1]):
            if start == destination:
                return 0
        INF = 10 ** 20

        costs = [[[INF for _ in range(len(DIRECTIONS))] for _ in range(M)] for _ in range(N)]

        q = collections.deque()
        q.append((start[0], start[1], 0))
        q.append((start[0], start[1], 1))
        q.append((start[0], start[1], 2))
        q.append((start[0], start[1], 3))
        costs[start[0]][start[1]][0] = 0
        costs[start[0]][start[1]][1] = 0
        costs[start[0]][start[1]][2] = 0
        costs[start[0]][start[1]][3] = 0
        ans = INF
        while len(q) > 0:
            size = len(q)
            for _ in range(size):
                y, x, d = q.popleft()
                dy, dx = DIRECTIONS[d]
                cost_here = costs[y][x][d]
                my, mx = y + dy, x + dx
                if isValidIdx(my, mx):
                    if cost_here + 1 < costs[my][mx][d]:
                        costs[my][mx][d] = cost_here + 1
                        q.append((my, mx, d))
                else:
                    # Stopped
                    if [y, x] == destination:
                        ans = min(ans, cost_here)
                    for i in range(len(DIRECTIONS)):
                        d = i
                        dy, dx = DIRECTIONS[i]
                        my, mx = y + dy, x + dx
                        if isValidIdx(my, mx):
                            if cost_here + 1 < costs[my][mx][d]:
                                costs[my][mx][d] = cost_here + 1
                                q.append((my, mx, d))
        if ans >= INF:
            return -1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class TheMazeIi(Solution):
    pass
