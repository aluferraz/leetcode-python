from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        N = len(nums)
        INF = 10 ** 20
        ans = INF
        windowSum = 0
        while right < N:
            windowSum += nums[right]
            while windowSum >= target and left <= right:
                ans = min(ans, (right - left + 1))
                windowSum -= nums[left]
                left += 1
            right += 1

        if ans == INF:
            return 0
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumSizeSubarraySum(Solution):
    pass
