from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        @cache
        def go(i, cur_target):
            if i == N:
                return cur_target == 0
            return  go(i+1, cur_target + nums[i]) + go(i+1, cur_target - nums[i])

        return go(0, target)


# leetcode submit region end(Prohibit modification and deletion)


class TargetSum(Solution):
    pass
