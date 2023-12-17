import math

import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        targets = []
        N = len(grid)
        M = len(grid[0])

        INF = 10 ** 20
        minY = INF
        maxY = -INF
        minX = INF
        maxX = -INF

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    minY = min(i, minY)
                    maxY = max(i, maxY)
                    minX = min(j, minX)
                    maxX = max(j, maxX)
                    targets.append((i, j))

        y = (maxY - minY) // 2
        x = (maxX - minX) // 2

        #
        #
        def get_cost(meeting):
            y, x = meeting
            if not (y >= 0 and y < N and x >= 0 and x < N):
                return INF
            cost = 0
            for u, v in targets:
                cost += abs(y - u) + abs(x - v)
            return cost

        ans = get_cost((y, x))

        y = int(math.ceil((maxY - minY) // 2))
        x = int(math.ceil((maxX - minX) // 2))
        ans = min(ans, get_cost((y, x)))

        return ans
        #
        # ans_cost = INF
        # ans = (-1, -1)
        # for i in range(N):
        #     for j in range(M):
        #         cost_here = get_cost((i, j))
        #         if cost_here < ans_cost:
        #             ans = (i, j)
        #             ans_cost = cost_here
        # return ans_cost

        # leetcode submit region end(Prohibit modification and deletion)


class BestMeetingPoint(Solution):
    pass
