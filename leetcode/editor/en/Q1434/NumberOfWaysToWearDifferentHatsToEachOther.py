from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numberWays(self, hats):
        """
        :type hats: List[List[int]]
        :rtype: int
        """
        N = len(hats)
        M = 41

        hatsAvailable = []
        for personHat in hats:
            hatsAvailable.append(set(personHat))
        @cache
        def go(hat, mask):
            if hat == M:
                return 1 if mask == ((1 << N) - 1) else 0
            ans = 0
            for x in range(N):
                if hat in hatsAvailable[x] and (mask & (1 << x)) == 0:
                    ans += go(hat + 1, mask | (1 << x))
            ans += go(hat + 1, mask)
            return ans

        return go(0, 0) % ((10 ** 9) + 7)


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfWaysToWearDifferentHatsToEachOther(Solution):
    pass
