# leetcode submit region begin(Prohibit modification and deletion)
from functools import cache


class Solution:
    def minSteps(self, N: int) -> int:
        INF = 10 ** 20

        @cache
        def go(prev, remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return INF
            paste = INF
            cp_jump = 1
            if prev != 0:
                paste = 1 + go(prev, remaining - prev)
                cp_jump = N - remaining

            copy_and_paste = 2 + go(cp_jump, remaining - cp_jump)
            return min(paste, copy_and_paste)

        return go(0, N - 1)


# leetcode submit region end(Prohibit modification and deletion)


class TwoKeysKeyboard(Solution):
    pass
