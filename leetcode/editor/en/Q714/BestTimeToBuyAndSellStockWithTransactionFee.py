from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        N = len(prices)
        INF = 10 ** 20

        cache = {}

        def best(i, canBuy):
            if i == N:
                return 0
            if (i, canBuy) in cache:
                return cache[(i, canBuy)]
            buy = -INF
            sell = -INF
            if canBuy:
                buy = -prices[i] + best(i + 1, False)
            else:
                sell = (prices[i] - fee) + best(i + 1, True)
            skip = best(i + 1, canBuy)
            ans = max(buy, skip, sell)
            cache[(i, canBuy)] = ans
            return ans

        return best(0, True)


# leetcode submit region end(Prohibit modification and deletion)


class BestTimeToBuyAndSellStockWithTransactionFee(Solution):
    pass
