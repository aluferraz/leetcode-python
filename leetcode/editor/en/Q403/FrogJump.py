from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        N = len(stones)

        stones_map = {}
        for i in range(N):
            stones_map[stones[i]] = i

        @cache
        def go(i, jump):
            if i == N - 1:
                return True
            ans = False
            if (stones[i] + jump) in stones_map and stones_map[(stones[i] + jump)] > i:
                ans = ans or go(stones_map[(stones[i] + jump)], jump)
            if i > 0 and jump > 1 and (stones[i] + jump - 1) in stones_map and stones_map[(stones[i] + jump - 1)] > i:
                ans = ans or go(stones_map[(stones[i] + jump - 1)], jump - 1)
            if i > 0 and (stones[i] + jump + 1) in stones_map and stones_map[(stones[i] + jump + 1)] > i:
                ans = ans or go(stones_map[(stones[i] + jump + 1)], jump + 1)
            return ans

        return go(0, 1)


# leetcode submit region end(Prohibit modification and deletion)


class FrogJump(Solution):
    pass
