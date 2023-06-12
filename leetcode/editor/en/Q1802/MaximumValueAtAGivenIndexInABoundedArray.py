from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxValue(self, N, index, maxSum):
        """
        :type N: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        left = 1
        right = maxSum

        def naturalSum(num):
            if num == 0:
                return 0
            return (num * (num + 1)) // 2

        def fill(num, size):
            if size == num:
                return naturalSum(num)
            if size > num:
                return naturalSum(num) + (size - num)
            if size < num:
                return naturalSum(num) - naturalSum(num - size)

        def good(num):
            leftSide = index
            rightSide = N - index - 1
            leftMinSum = fill(num - 1, leftSide)
            rightMinSum = fill(num - 1, rightSide)
            return (num + leftMinSum + rightMinSum) <= maxSum

        ans = -1
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MaximumValueAtAGivenIndexInABoundedArray(Solution):
    pass
