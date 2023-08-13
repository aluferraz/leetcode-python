from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coins.sort(reverse=True)
        cache = {}
        N = len(coins)

        def go(prev, k):
            if k == 0:
                return 1
            if (prev, k) in cache:
                return cache[(prev, k)]
            ans = 0
            for i in range(prev, N):
                if coins[i] <= k:
                    ans += go(i, k - coins[i])
            cache[(prev, k)] = ans
            return ans

        return go(0, amount)


# leetcode submit region end(Prohibit modification and deletion)


class CoinChangeIi(Solution):
    pass
