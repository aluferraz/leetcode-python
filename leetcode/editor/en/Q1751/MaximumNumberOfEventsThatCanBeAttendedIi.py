from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """

        events.sort()
        N = len(events)

        def find(target):
            left = 0
            right = N
            while left < right:
                mid = (left + right) // 2
                if events[mid][0] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        cache = [[None for _ in range(k + 1)] for _ in range(N)]

        def count(i, k):
            if i == N or k == 0:
                return 0
            if cache[i][k] is not None:
                return cache[i][k]

            (startDay, endDay, value) = events[i]
            use = value + count(find(endDay), k - 1)
            skip = count(i + 1, k)

            cache[i][k] = max(use, skip)
            return cache[i][k]

        return count(0, k)


# leetcode submit region end(Prohibit modification and deletion)


class MaximumNumberOfEventsThatCanBeAttendedIi(Solution):
    pass
