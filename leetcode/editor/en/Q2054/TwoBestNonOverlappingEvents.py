from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: (x[0], x[1], -x[2]))
        N = len(events)
        MAX_ALLOWED = 2

        def find(start):
            left = 0
            right = N
            while left < right:
                mid = (left + right) // 2
                if events[mid][0] > start:
                    right = mid
                else:
                    left = mid + 1
            return left

        @cache
        def go(i, remaining):
            ans = 0
            if i >= N or remaining == 0:
                return ans
            # take it
            next_idx = find(events[i][1])
            ans = events[i][2] + go(next_idx, remaining - 1)
            # skip it
            ans = max(ans, go(i + 1, remaining))
            return ans

        return go(0, MAX_ALLOWED)


# leetcode submit region end(Prohibit modification and deletion)


class TwoBestNonOverlappingEvents(Solution):
    pass
