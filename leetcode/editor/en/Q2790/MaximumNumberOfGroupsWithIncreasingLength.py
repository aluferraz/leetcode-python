import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        to_use = [[t, i] for (i, t) in enumerate(usageLimits)]
        to_use.sort()
        N = len(to_use)


        def next_non_breaking():
            left = 0
            right = N
            while left < right:
                mid = (left + right) // 2
                total, number = to_use[mid]
                if total <= 1:
                    left = mid + 1
                else:
                    right = mid
            return left

        def go(size, complement):
            group_size = 0
            used = 0
            if not complement:
                for _ in range(size):
                    i = next_non_breaking()
                    if i == N:
                        complement = True
                        break
                    to_use[i][0] -= 1
                    group_size += 1
                    number = to_use[i][1]
                    used |= (1 << number)
                    if group_size == size:
                        return 1 + go(size + 1, False)
            for i in range(N):
                t, n = to_use[i]
                if t == 0:
                    continue
                if used & (1 << n) == 0:
                    used |= (1 << n)
                    group_size += 1
                    to_use[i][0] -= 1
                if group_size == size:
                    return 1 + go(size + 1, True)
            return 0

        return go(1, False)

        # leetcode submit region end(Prohibit modification and deletion)


class MaximumNumberOfGroupsWithIncreasingLength(Solution):
    pass
