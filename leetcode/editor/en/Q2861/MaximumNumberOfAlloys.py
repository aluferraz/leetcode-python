from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
        """
        :type n: int
        :type k: int
        :type budget: int
        :type composition: List[List[int]]
        :type stock: List[int]
        :type cost: List[int]
        :rtype: int
        """

        def build_cost(machine_requirements, units):
            total_cost = 0
            material_need = [0] * n
            for i in range(n):
                material_need[i] = max((units * (machine_requirements[i]) - stock[i]), 0)
                total_cost += material_need[i] * cost[i]
            ans = total_cost <= budget
            return ans

        def can_build(machine):
            left = 0
            right = 10 ** 9
            ans = 0
            while left < right:
                mid = (left + right) // 2
                if build_cost(composition[machine], mid):
                    ans = mid
                    left = mid + 1
                else:
                    right = mid
            return ans

        ans = 0
        for i in range(k):
            ans = max(ans, can_build(i))
        return ans

    # leetcode submit region end(Prohibit modification and deletion)


class MaximumNumberOfAlloys(Solution):
    pass
