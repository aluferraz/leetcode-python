from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        left = 0
        right = x + 1
        ans = -1
        while left < right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Sqrtx(Solution):
    pass
