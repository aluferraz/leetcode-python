from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        N = len(nums)
        good = [0] * N
        good[0] = 1
        for i in range(1, N):
            if (nums[i - 1] % 2) != (nums[i] % 2):
                good[i] = 1
            else:
                good[i] = 0
        presum = [0] * N
        presum[0] = good[0]
        for i in range(1, N):
            presum[i] = presum[i - 1] + good[i]
        ans = []
        for f, t in queries:
            to_remove = presum[f]
            total_here = presum[t] - to_remove
            ans.append(total_here == (t - f))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SpecialArrayIi(Solution):
    pass
