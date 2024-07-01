import sortedcontainers

import collections
import heapq
from functools import cache
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """

        adj_list = collections.defaultdict(list)
        ans = [sortedcontainers.SortedSet() for _ in range(n)]
        inbound = [0] * n
        for u,v in edges:
            adj_list[u].append(v)
            inbound[v] += 1



        start_order = sortedcontainers.SortedList([(inbound[i], i) for i in range(n)] )

        while len(start_order) > 0:
            _, node = start_order[0]
            start_order.remove((_, node))
            for v in adj_list[node]:
                for x in ans[node]:
                    ans[v].add(x)
                start_order.remove( (inbound[v], v) )
                inbound[v] -= 1
                ans[v].add(node)
                start_order.add((inbound[v], v))




        return ans







# leetcode submit region end(Prohibit modification and deletion)


class AllAncestorsOfANodeInADirectedAcyclicGraph(Solution):
    pass
    