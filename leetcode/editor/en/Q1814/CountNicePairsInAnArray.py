import math

import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def rev(x):
            rev = list(str(x))
            rev.reverse()
            return int("".join(rev))

        cnt = collections.defaultdict(set)
        N = len(nums)
        for i in range(N):
            x = nums[i]
            diff = x - rev(x)
            cnt[diff].add(i)

        ans = 0
        MOD = 10 ** 9 + 7
        for k, v in cnt.items():
            size = len(v)
            ans += math.comb(size, 2) % MOD

        return ans % MOD


# leetcode submit region end(Prohibit modification and deletion)


class CountNicePairsInAnArray(Solution):
    pass
