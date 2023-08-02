import collections
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def minimumCosts(self, regular, express, expressCost):
        """
        :type regular: List[int]
        :type express: List[int]
        :type expressCost: int
        :rtype: List[int]
        """
        N = len(regular)
        INF = 10 ** 20

        dp = [[INF, INF] for _ in range(N + 1)]
        dp[0] = [0, expressCost]

        def count(i):
            if i == N:
                return 0
            # to arrive here, we've paid regular price
            stay_in_regular = regular[i] + dp[i][0]
            go_to_express = dp[i][0] + expressCost + express[i]
            stay_in_express = dp[i][1] + express[i]
            go_to_regular = dp[i][1] + regular[i]

            dp[i + 1][0] = min(stay_in_regular, go_to_regular)
            dp[i + 1][1] = min(stay_in_express, go_to_express)
            count(i + 1)

        count(0)
        ans = []
        for i in range(1, N + 1):
            ans.append(min(dp[i]))
        return ans
    #
    #
    # @cache
    # def go_regular(i):
    #     if i == N:
    #         return 0
    #
    #     stay_regular = go_regular(i + 1)
    #
    #     stay_express = go_express(i + 1)
    #
    #     best = min(regular[i] + stay_regular, expressCost + express[i] + stay_express)
    #
    #     # best_arrival[i] = min(best_arrival[i], stay_regular, stay_express)
    #
    #     return best
    #
    # @cache
    # def go_express(i):
    #     if i == N:
    #         return 0
    #
    #     stay_regular = go_regular(i + 1)
    #     stay_express = go_express(i + 1)
    #
    #     best = min(regular[i] + stay_regular, express[i] + stay_express)
    #     # best_arrival[i] = min(best_arrival[i], stay_regular, stay_express)
    #     return best


# leetcode submit region end(Prohibit modification and deletion)


class MinimumCostsUsingTheTrainLine(Solution):
    pass
