from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums.sort()
        N = len(nums)
        target = sum(nums) / k

        cache = {}

        def subsetSum(i, mask, currentSum, k):
            if k == 0:
                return True
            if currentSum == target:
                return subsetSum(0, mask, 0, k - 1)
            if currentSum > target or i == N:
                return False
            if (mask, currentSum) in cache:
                if cache[(mask, currentSum)]:
                    return subsetSum(0, mask, 0, k - 1)
                return False
            if mask & (1 << (i + 1)) == 0:
                if subsetSum(i + 1, mask | (1 << (i + 1)), currentSum + nums[i], k):
                    return True
            cache[(mask, currentSum)] = subsetSum(i + 1, mask, currentSum, k)
            return cache[(mask, currentSum)]

        return subsetSum(0, 0, 0, k)


# leetcode submit region end(Prohibit modification and deletion)


class PartitionToKEqualSumSubsets(Solution):
    pass
