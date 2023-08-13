from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximizeSweetness(self, sweetness, k):
        """
        :type sweetness: List[int]
        :type k: int
        :rtype: int
        """
        N = len(sweetness)

        def good(at_least_sweetness):
            slices = 0
            window_sum = 0
            for i in range(N):
                window_sum += sweetness[i]
                if window_sum >= at_least_sweetness:
                    slices += 1
                    window_sum = 0
            return slices >= k + 1

        left = 1
        right = sum(sweetness)
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if good(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

        # leetcode submit region end(Prohibit modification and deletion)


class DivideChocolate(Solution):
    pass
