# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1
        N = len(grid)
        M = len(grid[0])

        def isValidIdx(row, col):
            return 0 <= row < N and 0 <= col < M and grid[row][col] == 0

        DIRECTIONS = [
            [1, 0],
            [-1, 0],
            [1, 1],
            [1, -1],
            [-1, -1],
            [-1, 1],
            [0, 1],
            [0, -1],
        ]

        q = collections.deque()
        q.append([0, 0, 1])
        # found = False
        INF = 10 ** 20
        best = -1
        visited = set()
        visited.add((0, 0))

        while len(q) > 0:
            size = len(q)
            for _ in range(0, size):
                info = q.popleft()
                row = info[0]
                col = info[1]
                cost = info[2]
                if row == N - 1 and col == M - 1:
                    # best = min(best, cost)
                    # found = True
                    return cost

                for direction in DIRECTIONS:
                    newRow = row + direction[0]
                    newCol = col + direction[1]
                    if isValidIdx(newRow, newCol) and not (newRow, newCol) in visited:
                        visited.add((newRow, newCol))
                        q.append([newRow, newCol, cost + 1])

        return best

# leetcode submit region end(Prohibit modification and deletion)


class ShortestPathInBinaryMatrix(Solution):
    pass
