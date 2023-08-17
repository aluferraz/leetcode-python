import collections
from typing import List

import sortedcontainers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        window_sorted = sortedcontainers.SortedList()
        window = collections.deque()

        ans = []
        for (i, n) in enumerate(nums):
            window_sorted.add((-n, i))
            window.append((-n, i))
            if len(window_sorted) < k:
                continue
            ans.append(-window_sorted[0][0])
            window_sorted.remove(window.popleft())
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SlidingWindowMaximum(Solution):
    pass
