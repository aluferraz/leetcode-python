from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        N = len(nums)
        INF = 10 ** 20
        max_ahead = [-INF] * N
        min_behind = [INF] * N
        max_ahead[-1] = nums[-1]
        min_behind[0] = nums[0]

        for i in range(N - 2, -1, -1):
            max_ahead[i] = max(max_ahead[i + 1], nums[i])
        for i in range(1, N):
            min_behind[i] = min(min_behind[i - 1], nums[i])

        diff = -1
        for i in range(0, N - 1):
            if max_ahead[i + 1] > min_behind[i]:
                diff = max(diff, max_ahead[i + 1] - min_behind[i])

        return diff

        # leetcode submit region end(Prohibit modification and deletion)


class MaximumDifferenceBetweenIncreasingElements(Solution):
    pass
