from typing import List
from decimal import *


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        divisor = Decimal(1000)
        preprod = [1] * N
        preprod[0] = Decimal(nums[0])
        for i in range(1, N):
            preprod[i] = Decimal(preprod[i - 1] * nums[i])
        for i in range(N):
            preprod[i] /= divisor
        k = Decimal(k)


        def is_valid_range(left, right):
            dividend = (preprod[left - 1] * divisor if left > 0 else 1)
            total = (preprod[right] * divisor) / dividend
            return total < k
        ans = 0
        for i in range(N):
            left = i
            right = N
            while left < right:
                mid = (left + right) // 2
                if not is_valid_range(i, mid):
                    right = mid
                else:
                    left = mid + 1
            ans += (left - i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SubarrayProductLessThanK(Solution):
    pass
