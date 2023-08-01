from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == num:
                return True
            if mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False


# leetcode submit region end(Prohibit modification and deletion)


class ValidPerfectSquare(Solution):
    pass
