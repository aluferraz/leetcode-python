import collections
from functools import cache
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
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        edges = []
        seen = set()
        for i in range(N):
            for j in range(i, N):
                if i == j:
                    continue
                edges.append([i, j, manhattan_dist(points[i], points[j])])
        edges.sort(key=lambda x: x[2])

        parents = [-1] * N

        def find(i):
            while parents[i] >= 0:
                i = parents[i]
            return i

        def union(i, j):
            if i == j:
                return
            if parents[j] < parents[i]:
                return union(j, i)
            parents[i] += parents[j]
            parents[j] = i

        def kruskal():
            # nonlocal parents
            # nonlocal points
            ans = 0
            for u, v, w in edges:
                pu, pv = find(u), find(v)
                if pu == pv:
                    continue
                ans += w
                union(pu, pv)
            return ans

        ans = kruskal()

        return ans

    # leetcode submit region end(Prohibit modification and deletion)


class MinCostToConnectAllPoints(Solution):
    pass
