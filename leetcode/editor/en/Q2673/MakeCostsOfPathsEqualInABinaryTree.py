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
        #incomplete


        def min_cost(i):
            if (2 * i) + 1 > n:
                return 0
            left_idx = 2 * i
            right_idx = (2 * i) + 1
            lcost = cost[left_idx - 1] + min_cost(left_idx)
            rcost = cost[right_idx - 1] + min_cost(right_idx)
            cost_here = abs(lcost - rcost)

            return cost_here

        # return cost_here + min_cost(left_idx) + min_cost(right_idx)

        return min_cost(1)


# leetcode submit region end(Prohibit modification and deletion)


class MakeCostsOfPathsEqualInABinaryTree(Solution):
    pass
