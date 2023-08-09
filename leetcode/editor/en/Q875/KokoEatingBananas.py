import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        piles.sort()
        left = 1
        right = max(piles) + 1
        N = len(piles)

        def good(eats):
            time = 0
            for p in piles:
                time += math.ceil(p / eats)
            return time <= h

        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left


# leetcode submit region end(Prohibit modification and deletion)


class KokoEatingBananas(Solution):
    pass
