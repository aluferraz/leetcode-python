from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # nums.append(0)
        N = len(nums)

        def go(i, current):
            if i == N:
                return 0
            if current == -1:
                current = nums[i]
            if nums[i] & current == 0:
                return 1 + go(i + 1, -1)
            return go(i + 1, current & nums[i])

        return max(go(0, -1), 1)


# leetcode submit region end(Prohibit modification and deletion)


class SplitArrayIntoMaximumNumberOfSubarrays(Solution):
    pass
