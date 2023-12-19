from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])


# leetcode submit region end(Prohibit modification and deletion)


class MaximumProductDifferenceBetweenTwoPairs(Solution):
    pass
