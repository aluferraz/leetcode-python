from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        best = max(nums)
        ans = 0

        @cache
        def go(i):
            if i == N:
                return 0
            if nums[i] == best:
                return 1 + go(i + 1)
            return 0

        for i in range(N):
            ans = max(ans, go(i))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LongestSubarrayWithMaximumBitwiseAnd(Solution):
    pass
