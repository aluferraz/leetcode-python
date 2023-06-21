from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(nums)
        presum = [0 for _ in range(N)]
        ans = [-1 for _ in range(N)]
        presum[0] = nums[0]
        for i in range(1, N):
            presum[i] = presum[i - 1] + nums[i]

        for i in range(k, (N - k)):
            ans[i] = (presum[i + k] - (presum[i - k - 1] if i - k - 1 >= 0 else 0)) // ((2 * k) + 1)

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class KRadiusSubarrayAverages(Solution):
    pass
