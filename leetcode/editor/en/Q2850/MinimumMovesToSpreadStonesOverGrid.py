from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        zeros = []
        fillers = []

        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    zeros.append((i, j))
                if grid[i][j] > 0:
                    fillers.append((i, j))

        def manhattan_distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        INF = 10 ** 20

        def go(z_mask):
            if z_mask == ((1 << len(zeros)) - 1):
                return 0
            ans = INF
            for i in range(len(zeros)):
                if z_mask & (1 << i) == 0:
                    for j in range(len(fillers)):
                        u, v = fillers[j]
                        if grid[u][v] > 1:
                            grid[u][v] -= 1
                            use_filler = manhattan_distance(zeros[i], fillers[j]) + go(z_mask | (1 << i))
                            ans = min(ans, use_filler)
                            grid[u][v] += 1
            return ans

        return go(0)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumMovesToSpreadStonesOverGrid(Solution):
    pass
