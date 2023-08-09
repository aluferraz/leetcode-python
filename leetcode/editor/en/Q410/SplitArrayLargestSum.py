from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        INF = 10 ** 20
        N = len(nums)
        presum = [0] * N
        presum[0] = nums[0]
        for i in range(1, N):
            presum[i] = presum[i - 1] + nums[i]

        dp = [
            [
                [
                    [
                        INF
                    ] for _ in range(N)
                ] for _ in range(N)
            ] for _ in range(k + 1)
        ]

        #to be continued

    # leetcode submit region end(Prohibit modification and deletion)


class SplitArrayLargestSum(Solution):
    pass
