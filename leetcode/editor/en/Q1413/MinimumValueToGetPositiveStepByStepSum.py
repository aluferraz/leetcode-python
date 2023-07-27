from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        right = 10**5

        def good(value):
            current = value
            for n in nums:
                current += n
                if current <= 0:
                    return False
            return True

        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left


# leetcode submit region end(Prohibit modification and deletion)


class MinimumValueToGetPositiveStepByStepSum(Solution):
    pass
