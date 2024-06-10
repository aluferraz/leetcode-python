import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = collections.Counter()
        seen[0] += 1
        current = 0
        N = len(nums)
        ans = 0
        for i in range(N):
            current += nums[i]
            current %= k
            if current in seen:
                ans += seen[current]
            seen[current] += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SubarraySumsDivisibleByK(Solution):
    pass
