import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left = 1
        right = max(nums) + 1

        def good(div):
            tot = 0
            for n in nums:
                tot += math.ceil(n / div)
            return tot <= threshold

        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1

        return left


# leetcode submit region end(Prohibit modification and deletion)


class FindTheSmallestDivisorGivenAThreshold(Solution):
    pass
