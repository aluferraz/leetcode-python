from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        N = len(piles)
        left = 0
        right = N - 1
        ans = 0
        while left <= right:
            alice = piles[right]
            right -= 1
            me = piles[right]
            right -= 1
            bob = piles[left]
            left += 1
            ans += me
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MaximumNumberOfCoinsYouCanGet(Solution):
    pass
