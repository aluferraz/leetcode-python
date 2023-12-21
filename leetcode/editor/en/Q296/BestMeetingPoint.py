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
        ys = []
        xs = []

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    ys.append(i)
                    xs.append(j)

        ys.sort()
        xs.sort()

        ans = 0
        y = ys[len(ys) // 2]
        x = xs[len(xs) // 2]

        for i in ys:
            ans += abs(y - i)
        for i in xs:
            ans += abs(x - i)

        return ans

        # leetcode submit region end(Prohibit modification and deletion)


class BestMeetingPoint(Solution):
    pass
