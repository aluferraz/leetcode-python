import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minIncrements(self, n, cost):
        """
        :type n: int
        :type cost: List[int]
        :rtype: int
        """
        ans = 0

        def min_cost(i, p):
            if i + 1 > n or (2 * i) + 1 > n:
                return cost[i - 1]
            nonlocal ans
            left_idx = 2 * i
            right_idx = (2 * i) + 1

            total_cost = min_cost(left_idx, i)
            total_cost += min_cost(right_idx, i)

            cost_here = abs(cost[right_idx - 1] - cost[left_idx - 1])
            cost[i - 1] += max(cost[right_idx - 1], cost[left_idx - 1])
            ans += cost_here
            return cost_here

        min_cost(1, 0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MakeCostsOfPathsEqualInABinaryTree(Solution):
    pass
