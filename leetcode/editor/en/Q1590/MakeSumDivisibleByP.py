from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        diff = sum(nums) % p
        if diff == 0:
            return 0
        N = len(nums)
        presum = list(nums)
        for i in range(1, N):
            presum[i] = presum[i - 1] + nums[i]

        def can_make_it(i):
            left = 0
            right = N - i - 1
            left_side = (presum[i - 1] if i > 0 else 0)
            tot = presum[-1]
            while left < right:
                mid = (left + right) // 2
                to_remove = (presum[i + mid] - left_side)
                if (tot - to_remove) % p > 0:
                    left = mid + 1
                else:
                    right = mid
            to_remove = (presum[i + left] - left_side)
            if (tot - to_remove) % p == 0:
                return left + 1
            return N

        ans = N
        for i in range(N):
            ans = min(ans, can_make_it(i))
        if ans == N:
            return -1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MakeSumDivisibleByP(Solution):
    pass
