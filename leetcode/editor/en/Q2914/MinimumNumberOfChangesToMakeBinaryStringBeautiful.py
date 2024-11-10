# leetcode submit region begin(Prohibit modification and deletion)
from functools import cache


class Solution:
    def minChanges(self, s: str) -> int:
        N = len(s)

        @cache
        def go(i, t):
            if i == N:
                return 0
            changes = 0
            if int(s[i]) != t:
                changes += 1
            ans = go(i + 1, t)  # do not split
            if (i + 1) % 2 == 0:
                ans = min(ans, go(i + 1, (t + 1) % 2))
            return changes + ans

        s_zero = go(0, 0)
        s_one = go(0, 1)
        return min(s_zero, s_one)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumNumberOfChangesToMakeBinaryStringBeautiful(Solution):
    pass
