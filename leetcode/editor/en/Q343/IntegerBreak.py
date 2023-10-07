import math

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = [0] * (n + 1)
        has_cache = [False] * (n + 1)

        def go(x):
            if x == 0:
                return 0
            if x <= 2:
                return 1
            if has_cache[x]:
                return cache[x]
            best = 0
            for i in range(1, math.ceil(x / 2) + 1):
                diff = x - i
                break_or_keep = max(diff, go(diff))
                best = max(best,
                           break_or_keep * i,
                           )
            cache[x] = best
            has_cache[x] = True
            return best

        return go(n)


# leetcode submit region end(Prohibit modification and deletion)


class IntegerBreak(Solution):
    pass
