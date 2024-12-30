from functools import cache
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        @cache
        def go(size):
            if size > high:
                return 0
            ans = 0
            if size + zero <= high:
                if size + zero >= low:
                    ans += 1
                ans = (ans + go(size + zero)) % MOD
            if size + one <= high:
                if size + one >= low:
                    ans += 1
                ans = (ans + go(size + one)) % MOD
            return ans % MOD
        return go(0) % MOD

        
# leetcode submit region end(Prohibit modification and deletion)


class CountWaysToBuildGoodStrings(Solution):
    pass
    