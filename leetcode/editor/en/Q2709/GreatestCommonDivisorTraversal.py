import collections
import math
from functools import cache
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        N = len(nums)
        target_mask = (1 << N) - 1
        mask = 0 | (1 << 0)

        def solve(i):
            nonlocal mask
            if mask == target_mask:
                return True

            ans = False

            for j in range(N):
                if j != i and (1 << j) & mask == 0:
                    can_jump = math.gcd(nums[i], nums[j]) > 1
                    if can_jump:
                        mask |= mask | 1 << j
                        ans = solve(j)
                        if ans:
                            break
            return ans

        solve(0)
        return mask == target_mask



# leetcode submit region end(Prohibit modification and deletion)


class GreatestCommonDivisorTraversal(Solution):
    pass