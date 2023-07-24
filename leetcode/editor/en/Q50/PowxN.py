from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        dp = {}
        dp[0] = 1
        dp[1] = x

        current = 1
        while current * 2 < abs(n):
            dp[current * 2] = dp[current] * dp[current]
            current *= 2

        remaining = abs(n) - current

        dp[n] = dp[current] * self.myPow(x, remaining)

        return dp[n] if n > 0 else 1 / dp[n]

    # leetcode submit region end(Prohibit modification and deletion)


class PowxN(Solution):
    pass
