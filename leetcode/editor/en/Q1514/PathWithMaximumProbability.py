import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        N = n

        queue = collections.deque()

        adj_list = collections.defaultdict(set)
        parents = [-1 for _ in range(N)]

        def find(i):
            pathComp = collections.deque()
            while parents[i] >= 0:
                pathComp.append(i)
                i = parents[i]
            while len(pathComp) > 0:
                comp = pathComp.pop()
                if parents[comp] >= 0:
                    parents[comp] = i
            return i

        def union(i, j):
            if i == j:
                return
            if parents[j] < parents[i]:
                return union(j, i)
            parents[i] += parents[j]
            parents[j] = i

        for i, (u, v) in enumerate(edges):
            adj_list[u].add((succProb[i], v))
            adj_list[v].add((succProb[i], u))
            union(find(u), find(v))

        if find(start) != find(end):
            return 0

        INF = 10 ** 20
        cost = [(-1, end)]
        ans = -1
        seen = collections.defaultdict(lambda: -INF)
        seen[end] = 1

        while len(cost) > 0:
            (prob, node) = heapq.heappop(cost)
            connections = adj_list[node]
            for (nextProb, nextConn) in connections:
                totalProb = abs(prob * nextProb)
                if seen[nextConn] < totalProb:  # better path
                    seen[nextConn] = totalProb
                    heapq.heappush(cost, (-totalProb, nextConn))
        if start in seen:
            return seen[start]
        return 0


# leetcode submit region end(Prohibit modification and deletion)


class PathWithMaximumProbability(Solution):
    pass
