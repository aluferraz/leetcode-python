from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        abs_diff = 0
        N = len(nums)
        presum = [0] * N
        presum[0] = nums[0]
        for i in range(1, N):
            presum[i] = presum[i - 1] + nums[i]

        ans = [-1] * N
        ahead = 0
        for i in range(N - 1, -1, -1):
            if i + 1 < N:
                elements_ahead = (N - 1 - i)
                diff = abs(nums[i] - ahead)
                abs_diff += (diff * (elements_ahead - 1)) + diff
            ans_here = abs(((i + 1) * nums[i]) - (presum[i])) + abs_diff
            ans[i] = ans_here
            ahead = nums[i]

        return ans

        # leetcode submit region end(Prohibit modification and deletion)


class SumOfAbsoluteDifferencesInASortedArray(Solution):
    pass
