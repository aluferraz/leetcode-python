from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minOperations(self, s1, s2, x):
        """
        :type s1: str
        :type s2: str
        :type x: int
        :rtype: int
        """
        N = len(s1)
        INF = 10 ** 20

        def flip(x):
            return str((int(x) + 1) % 2)

        @cache
        def go(i, reversed, has_credit):
            if i == N:
                return 0 if not reversed and not has_credit else INF
            c = s1[i]
            if reversed:
                c = flip(c)
            if c == s2[i]:
                return go(i + 1, False, has_credit)
            ans = INF

            ans = min(ans,
                      1 + go(i + 1, True, has_credit)
                      )
            ans = min(ans, (0 if has_credit else x) + go(i + 1, False, (not has_credit)))
            return ans

        ans = go(0, False, False)
        if ans >= INF:
            return -1
        return ans
        # leetcode submit region end(Prohibit modification and deletion)


class ApplyOperationsToMakeTwoStringsEqual(Solution):
    pass
