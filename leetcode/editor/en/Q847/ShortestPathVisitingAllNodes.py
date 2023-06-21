import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        adj_list = collections.defaultdict(set)
        N = len(graph)
        INF = 10 ** 10
        for i in range(N):
            for n in graph[i]:
                adj_list[i].add(n)
                adj_list[n].add(i)
        allVisited = (1 << N) - 1
        cache = {}

        def dfs(node, mask):
            if mask == allVisited:
                return 0
            state = (node, mask)
            if state in cache:
                return cache[state]

            cache[state] = INF  # Since we can revisit the same node, let's cache the bitmask as infinity.
            # So we can only proceed on the recursion if I visited at least one new node (hences the mask will be diff)
            # This avoids infinite loops

            for v in adj_list[node]:
                # if mask | ( 1 << v ) == 0: We can revisit the same node
                already_visited = 1 + dfs(v, mask)
                unvisited = 1 + dfs(v, mask | (1 << v))
                cache[state] = min( cache[state], already_visited, unvisited)
            cache[state] = cache[state]
            return cache[state]

        ans = INF

        for i in range(N):
            ans = min(ans, dfs(i, (1 << i)))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class ShortestPathVisitingAllNodes(Solution):
    pass
