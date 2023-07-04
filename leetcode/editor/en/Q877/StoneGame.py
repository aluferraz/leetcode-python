from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        @cache
        def play(left, right):
            if left > right:
                return 0
            takeLeft = piles[left] - play(left + 1, right)
            takeRight = piles[right] - play(left, right - 1)
            return max(takeLeft, takeRight)

        return play(0, len(piles) - 1) > 0


# leetcode submit region end(Prohibit modification and deletion)


class StoneGame(Solution):
    pass
