from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        def natural_sum(n):
            return (n * (n + 1)) // 2

        left = 1
        right = n + 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if natural_sum(mid) <= n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class ArrangingCoins(Solution):
    pass
