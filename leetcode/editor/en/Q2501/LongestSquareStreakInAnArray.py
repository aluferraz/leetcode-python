import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        nums = sorted(set(nums), reverse=True)
        chains = collections.defaultdict(int)
        for n in nums:
            squared = (n ** 2)
            tot = 0
            if squared in chains:
                tot = chains[squared]
                chains.pop(squared)
            chains[n] = tot + 1
        ans = max(chains.values())
        if ans == 1:
            return -1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LongestSquareStreakInAnArray(Solution):
    pass
