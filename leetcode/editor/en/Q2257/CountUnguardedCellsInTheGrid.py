import collections
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        FREE = 1
        matrix = [[1 for _ in range(n)] for _ in range(m)]

        DIRECTIONS = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0],
        ]
        queue = collections.deque()
        for i,j in guards:
            matrix[i][j] = 0
            for k in range(len(DIRECTIONS)):
                queue.append((i,j,k))

        walls = set( (y,x) for y,x in walls )
        enqueued = set()
        for i,j in walls:
            matrix[i][j] = -1
        def is_valid_idx(i,j):
            return i >= 0 and i < m and j >= 0 and j < n and (i,j) not in walls
        while queue:
            size = len(queue)
            for _ in range(size):
                i,j,k = queue.popleft()
                matrix[i][j] = 0
                di,dj = DIRECTIONS[k]
                if is_valid_idx(i+di, j + dj):
                    if (i+di, j + dj, k) not in enqueued:
                        enqueued.add((i+di, j + dj, k))
                        queue.append((i+di, j + dj, k))
        for i,j in walls:
            matrix[i][j] = 0
        ans = 0
        for row in matrix:
            ans += sum(row)
        return ans



# leetcode submit region end(Prohibit modification and deletion)


class CountUnguardedCellsInTheGrid(Solution):
    pass
    