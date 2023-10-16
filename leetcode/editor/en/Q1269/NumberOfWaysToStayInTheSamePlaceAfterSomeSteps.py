from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        MOD = (10 ** 9) + 7
        N = arrLen

        cache = {}

        def go(i, s):
            if s == 0:
                return 1 if i == 0 else 0
            if (i, s) in cache:
                return cache[(i, s)]

            stay = go(i, s - 1)
            right = 0
            left = 0
            if i + 1 < N and s > i + 1:
                right = go(i + 1, s - 1)
            if i - 1 >= 0:
                left = go(i - 1, s - 1)
            ans = stay + right + left

            cache[(i, s)] = ans % MOD
            return ans

        return go(0, steps) % MOD


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfWaysToStayInTheSamePlaceAfterSomeSteps(Solution):
    pass
