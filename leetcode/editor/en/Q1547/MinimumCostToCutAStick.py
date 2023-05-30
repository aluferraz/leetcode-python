# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        cuts = set(cuts)
        cuts.add(0)
        cuts.add(n)
        cuts = list(cuts)
        cuts.sort()

        cache = {}

        def minCuts(left, right):
            if (left + 1 >= right):
                return 0
            key = (left, right)
            if key in cache:
                return cache[key]

            cost = cuts[right] - cuts[left]
            best = 10 ** 20
            for i in range(left + 1, right):
                best = min(best, cost + minCuts(left, i) + minCuts(i, right))
            cache[key] = best
            return best

        return minCuts(0, len(cuts) - 1)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumCostToCutAStick(Solution):
    pass
