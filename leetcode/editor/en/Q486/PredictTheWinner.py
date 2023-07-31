from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        cache = {}
        N = len(nums)

        def canWin(left, right):
            best = 0
            if left > right:
                return best
            if (left, right) in cache:
                return cache[(left, right)]

            best = max(
                nums[left] - canWin(left + 1, right),
                nums[right] - canWin(left, right - 1)
            )

            cache[(left, right)] = best
            return best

        return canWin(0, N - 1) >= 0


# leetcode submit region end(Prohibit modification and deletion)


class PredictTheWinner(Solution):
    pass
