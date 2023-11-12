import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Graph(object):

    def __init__(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        """
        self.N = n
        self.adj_list = collections.defaultdict(list)
        for u, v, c in edges:
            self.adj_list[u].append((v, c))

    def addEdge(self, edge):
        """
        :type edge: List[int]
        :rtype: None
        """
        u, v, c = edge
        self.adj_list[u].append((v, c))

    def shortestPath(self, node1, node2):
        """
        :type node1: int
        :type node2: int
        :rtype: int
        """
        INF = 10 ** 20
        N = self.N
        adj_list = self.adj_list
        visited = [INF] * N
        to_discover = [(0, node1)]
        visited[node1] = 0
        ans = -1
        while len(to_discover) > 0 and to_discover[0][0] < INF:
            _, current = heapq.heappop(to_discover)
            if current == node2:
                ans = visited[current]
                return ans
            for v, c in adj_list[current]:
                total_cost = visited[current] + c
                if total_cost < visited[v]:
                    heapq.heappush(to_discover, (total_cost, v))
                    visited[v] = total_cost

        return ans


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
# leetcode submit region end(Prohibit modification and deletion)


class DesignGraphWithShortestPathCalculator(Graph):
    pass
