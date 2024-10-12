from bisect import bisect_left
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        s = []
        res = 0
        for i in range(len(nums)):
            if not s or nums[s[-1]] > nums[i]:
                s.append(i)
            pos = bisect_left(s, -nums[i], key=lambda j: -nums[j])
            res = max(res, i - s[pos])
        return res


# leetcode submit region end(Prohibit modification and deletion)


class MaximumWidthRamp(Solution):
    pass
