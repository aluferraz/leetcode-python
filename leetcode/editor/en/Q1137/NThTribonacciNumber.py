from functools import cache


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def go(num):
            if num == 0:
                return 0
            if num == 1:
                return 1
            if num == 2:
                return 1
            return go(num - 1) + go(num - 2) + go(num - 3)

        return go(n)


# leetcode submit region end(Prohibit modification and deletion)


class NThTribonacciNumber(Solution):
    pass
