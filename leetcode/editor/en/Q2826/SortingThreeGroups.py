from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)

        def lis():
            dp = [1] * N
            for i in range(N):
                for j in range(i - 1, -1, -1):
                    if nums[i] >= nums[j]:
                        dp[i] = max(dp[i], 1 + dp[j])
            return max(dp)

        return N - lis()


# leetcode submit region end(Prohibit modification and deletion)


class SortingThreeGroups(Solution):
    pass
