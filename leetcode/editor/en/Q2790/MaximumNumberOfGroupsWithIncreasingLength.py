import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        N = len(usageLimits)
        usageLimits.sort()

        for i in range(N):
            usageLimits[i] = min(usageLimits[i], N)

        def can_create(groups):
            required = 0
            for i in range(N - 1, -1, -1):
                if groups > 0:
                    required += groups
                    groups -= 1
                required -= min(required,
                                usageLimits[i])  # the key is to never take more than the required, to avoid duplicates
            return required == 0

        left = 1
        right = N
        ans = 1
        while left <= right:
            mid = (left + right) // 2
            if can_create(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

        # leetcode submit region end(Prohibit modification and deletion)


class MaximumNumberOfGroupsWithIncreasingLength(Solution):
    pass
