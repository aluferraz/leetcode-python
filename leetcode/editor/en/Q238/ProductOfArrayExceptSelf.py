from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix_prod = list(nums)
        prefix_prod = list(nums)
        N = len(nums)
        for i in range(1, N):
            prefix_prod[i] = prefix_prod[i - 1] * nums[i]
        for i in range(N - 2, -1, -1):
            suffix_prod[i] = suffix_prod[i + 1] * nums[i]

        ans = [1] * N
        for i in range(N):
            pref = prefix_prod[i - 1] if i > 0 else 1
            suff = suffix_prod[i + 1] if i < N - 1 else 1
            ans[i] = pref * suff
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class ProductOfArrayExceptSelf(Solution):
    pass
