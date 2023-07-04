import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        edges = list(zip(nums, cost))
        edges.sort()
        N = len(nums)

        distBehind = [0 for _ in range(N)]
        dp = [0 for _ in range(N)]
        costAhead = 0

        for i in range(1, N):
            distBehind[i] = distBehind[i - 1] + (edges[i][0] - edges[i - 1][0])

        for i in range(1, N):
            dp[0] += distBehind[i] * edges[i][1]
            costAhead += edges[i][1]
        costBehind = edges[0][1]
        for i in range(1, N):
            newDistance = edges[i][0] - edges[i - 1][0]
            dp[i] = dp[i - 1] - (newDistance * costAhead)
            dp[i] += (newDistance * costBehind)
            costBehind += edges[i][1]
            costAhead -= edges[i][1]

        return min(dp)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumCostToMakeArrayEqual(Solution):
    pass
