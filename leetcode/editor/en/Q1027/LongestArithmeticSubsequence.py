from bisect import bisect_left
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        limit = max(nums) + 1
        N = len(nums)
        counter = [0 for _ in range(limit)]
        maxCounter = 0
        for i in range(N):
            counter[nums[i]] += 1
            maxCounter = max(maxCounter, counter[nums[i]])
        best = self.lasHelper(nums, limit)
        nums.reverse()
        best = max(best, self.lasHelper(nums, limit), maxCounter)
        return best

    def lasHelper(self, nums, limit):
        N = len(nums)
        dp = [[0 for _ in range(limit)] for _ in range(limit)]

        for i in range(N):
            dp[nums[i]] = [1 for _ in range(limit)]

            for j in range(1, nums[i] + limit):
                if (nums[i] - j) >= 0:
                    dp[nums[i]][j] += dp[nums[i] - j][j]
                else:
                    break
        best = 0
        for las in dp:
            best = max(best, max(las))
        return best


# leetcode submit region end(Prohibit modification and deletion)


class LongestArithmeticSubsequence(Solution):
    pass
