from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        target = [0] * 32
        current = [0] * 32
        for i in range(32):
            target[i] = min((1 << i) & k, 1)
        current_xor = nums[0]
        N = len(nums)
        for i in range(1, N):
            current_xor ^= nums[i]
        for i in range(32):
            current[i] = min((1 << i) & current_xor, 1)
        ans = 0
        for i in range(32):
            if current[i] != target[i]:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumNumberOfOperationsToMakeArrayXorEqualToK(Solution):
    pass
