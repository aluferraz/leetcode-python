from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        N = len(points)
        INF = 10 ** 20

        def manhattan_dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1], b[1])

        @cache
        def go(i, p, mask):
            if mask == ((1 << N) - 1):
                return 0
            ans = INF
            for j in range(N):
                if j & (1 << j) != 0 or j == p:
                    continue
                ans = min(ans,
                          manhattan_dist(points[i], points[j]) +
                          go(j, i, mask | (1 << j))
                          )
            return ans

        ans = INF

        for i in range(N):
            ans = min(ans,
                      go(i, i, 0)
                      )
        return ans

    # leetcode submit region end(Prohibit modification and deletion)


class MinCostToConnectAllPoints(Solution):
    pass
