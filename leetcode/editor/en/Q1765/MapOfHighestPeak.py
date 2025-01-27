import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        N = len(isWater)
        M = len(isWater[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isValidIdx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M

        ans = [[0 for _ in range(M)] for _ in range(N)]
        visited = set()
        q = collections.deque()
        for i in range(N):
            for j in range(M):
                if isWater[i][j] == 1:
                    q.append((i, j))
                    visited.add((i, j))

        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                can_be = ans[i][j] + 1
                for di, dj in DIRECTIONS:
                    if isValidIdx(i + di, j + dj) and (i + di, j + dj) not in visited:
                        ans[i + di][j + dj] = can_be
                        q.append((i + di, j + dj))
                        visited.add((i + di, j + dj))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MapOfHighestPeak(Solution):
    pass
