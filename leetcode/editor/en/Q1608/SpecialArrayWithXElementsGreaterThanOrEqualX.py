import bisect
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        for x in range(1, N + 1):
            cnt = bisect.bisect_left(nums, x)
            if (N - cnt) == x:
                return x
        return -1


# leetcode submit region end(Prohibit modification and deletion)


class SpecialArrayWithXElementsGreaterThanOrEqualX(Solution):
    pass
