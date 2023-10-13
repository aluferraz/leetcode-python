from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        N = len(cost)

        has_cache = [False] * N
        cache = [0] * N

        def go(i):
            if i >= N:
                return 0
            if has_cache[i]:
                return cache[i]
            one_step = cost[i] + go(i + 1)
            two_step = cost[i] + go(i + 2)
            has_cache[i] = True
            cache[i] = min(one_step, two_step)
            return cache[i]

        return min(go(0), go(1))


# leetcode submit region end(Prohibit modification and deletion)


class MinCostClimbingStairs(Solution):
    pass
