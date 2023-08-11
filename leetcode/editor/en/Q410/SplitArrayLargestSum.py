from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        N = len(nums)

        def good(ans):
            current_slice_tot = 0
            slices = 1

            for i in range(N):
                if current_slice_tot + nums[i] <= ans and (i + k - slices) < N:
                    current_slice_tot += nums[i]
                else:
                    if nums[i] > ans:
                        return False
                    slices += 1
                    current_slice_tot = nums[i]
            return slices == k

        left = min(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left


# leetcode submit region end(Prohibit modification and deletion)


class SplitArrayLargestSum(Solution):
    pass
