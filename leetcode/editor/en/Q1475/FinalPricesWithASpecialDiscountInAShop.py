from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        N = len(prices)
        NLE = [ N ] * N
        stack = []
        for i in range(N):
            while stack and prices[i] <= prices[stack[-1]]:
                NLE[stack.pop()] = i
            stack.append(i)
        prices.append(0)
        ans = [0] * N
        for i in range(N):
            ans[i] = prices[i] - prices[NLE[i]]
        return ans




# leetcode submit region end(Prohibit modification and deletion)


class FinalPricesWithASpecialDiscountInAShop(Solution):
    pass
    