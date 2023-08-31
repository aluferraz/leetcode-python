import collections
import math
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        N = len(nums)
        mono_increasing = collections.deque(nums)
        ans = 0
        min_seen = mono_increasing[-1]

        INF = 10 ** 20

        def go(i, min_seen):
            if i == -1:
                return 0

            if nums[i] > min_seen:
                new_min = nums[i] // math.ceil(nums[i] / min_seen)
                ans = math.ceil(nums[i] / min_seen) - 1 + go(i - 1, min(min_seen, new_min))
                return ans
            return go(i - 1, min(min_seen, nums[i]))

        return go(N - 1, min_seen)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumReplacementsToSortTheArray(Solution):
    pass
