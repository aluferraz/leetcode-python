import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        presum = [0] * N
        presum[0] = nums[0]
        for i in range(1, N):
            presum[i] = presum[i - 1] + nums[i]
        ans = 0
        seen_extra_zeros = {}
        seen_extra_ones = {}
        for i in range(N):
            length = (i+1)
            total_ones = presum[i]
            total_zeros = length - total_ones
            if total_ones == total_zeros:
                ans = max(ans, length)
            elif total_zeros > total_ones:
                extra_zeros = total_zeros - total_ones
                if extra_zeros in seen_extra_zeros:
                    start = seen_extra_zeros[extra_zeros]
                    length = i - start
                    if length % 2 == 0 and presum[i] - presum[start] == length // 2:
                        ans = max(ans, length)
                else:
                    seen_extra_zeros[extra_zeros] = i
            else:
                extra_ones = total_ones - total_zeros
                if extra_ones in seen_extra_ones:
                    start = seen_extra_ones[extra_ones]
                    length = i - start
                    if length % 2 == 0 and presum[i] - presum[start] == length // 2:
                        ans = max(ans, length)
                else:
                    seen_extra_ones[extra_ones] = i
        return ans

# leetcode submit region end(Prohibit modification and deletion)


class ContiguousArray(Solution):
    pass
