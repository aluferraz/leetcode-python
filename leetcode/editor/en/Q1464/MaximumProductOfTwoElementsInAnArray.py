from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return (nums[-2] - 1) * (nums[-1] - 1)


# leetcode submit region end(Prohibit modification and deletion)


class MaximumProductOfTwoElementsInAnArray(Solution):
    pass
