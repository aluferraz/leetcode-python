import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        N = len(nums)
        DP = [collections.defaultdict(int) for _ in range(N)]
        ans = 0
        for i in range(1,N):
            for j in range(i):
                d = nums[i] - nums[j]
                ans += DP[j][d]
                DP[i][d] += 1 + DP[j][d]

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class ArithmeticSlicesIiSubsequence(Solution):
    pass
