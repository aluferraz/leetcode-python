import collections
import heapq
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        if p == 0:
            return 0
        nums.sort()
        N = len(nums)

        def good(ans):
            tot = 0
            used = [False] * N
            for i in range(0, N - 1):
                if used[i]:
                    continue
                if abs(nums[i + 1] - nums[i]) <= ans:
                    used[i] = True
                    used[i + 1] = True

                    tot += 1
            return tot >= p

        left = 0
        right = 10 ** 9 + 1

        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left


# leetcode submit region end(Prohibit modification and deletion)


class MinimizeTheMaximumDifferenceOfPairs(Solution):
    pass
