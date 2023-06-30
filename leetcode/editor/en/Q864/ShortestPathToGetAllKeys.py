import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        startPos = (0, 0)
        N = len(grid)
        M = len(grid[0])
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        keysMask = 0

        def isValidIdx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M

        for i in range(N):
            newRow = []
            for j in range(M):
                newRow.append(grid[i][j])
                if grid[i][j] == '@':
                    startPos = (i, j)
                if grid[i][j].isalpha():
                    if grid[i][j].islower():
                        keysMask |= 1 << (ord(grid[i][j]) - ord('a'))
            grid[i] = newRow
        visited = set()

        queue = collections.deque()
        queue.append((startPos, 0, 0))
        visited.add((startPos[0], startPos[1], 0))
        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                (row, col), keys, moves = queue.popleft()

                if grid[row][col].islower():
                    keys |= (1 << (ord(grid[row][col]) - ord('a')))
                if keys == keysMask:
                    return moves

                for (y, x) in DIRECTIONS:
                    if isValidIdx(row + y, col + x):
                        if grid[row + y][col + x] == '#':
                            continue
                        if grid[row + y][col + x].isupper():
                            matchingKey = (1 << (ord(grid[row + y][col + x].lower()) - ord('a')))
                            if keys & matchingKey == 0:
                                continue
                        if not (row + y, col + x, keys) in visited:
                            visited.add((row + y, col + x, keys))
                            queue.append(
                                ((row + y, col + x), keys, moves + 1)
                            )
        return -1


# leetcode submit region end(Prohibit modification and deletion)


class ShortestPathToGetAllKeys(Solution):
    pass
