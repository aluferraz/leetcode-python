import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """

        DIRECTIONS = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        visited = set()

        def isValidIdx(y, x):
            return isValidCoord(y, x) and (maze[y][x] == 0)

        def isValidCoord(y, x):
            return (y >= 0 and y < len(maze) and x >= 0 and x < len(maze[0]))

        def dfs(y, x, d):

            if not isValidIdx(y, x) or (y, x, d) in visited:
                return False
            visited.add((y, x, d))
            u, v = DIRECTIONS[d]
            if (y, x) == (destination[0], destination[1]):
                if not isValidIdx(y + u, x + v):
                    return True

            if dfs(y + u, x + v, d):
                return True
            else:
                if not isValidIdx(y + u, x + v):
                    for i in range(len(DIRECTIONS)):
                        u, v = DIRECTIONS[i]
                        if isValidIdx(y + u, x + v) and (y + u, x + v, i) not in visited:
                            if dfs(y + u, x + v, i):
                                return True
                return False

        for i in range(len(DIRECTIONS)):
            if dfs(start[0], start[1], i):
                return True
        return False


# leetcode submit region end(Prohibit modification and deletion)


class TheMaze(Solution):
    pass
