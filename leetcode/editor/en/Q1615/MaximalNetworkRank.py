import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        if len(roads) == 0:
            return 0
        N = n
        ranks = [0] * N
        roads_double = set()
        for (u, v) in roads:
            ranks[u] += 1
            ranks[v] += 1
            roads_double.add((min(u, v), max(u, v)))

        best = 0
        for i in range(N):
            for j in range(i + 1, N):
                if (i, j) in roads_double:
                    best = max(best, ranks[i] + ranks[j] - 1)
                else:
                    best = max(best, ranks[i] + ranks[j])

        return best


# leetcode submit region end(Prohibit modification and deletion)


class MaximalNetworkRank(Solution):
    pass
