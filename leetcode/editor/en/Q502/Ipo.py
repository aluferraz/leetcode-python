from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        best_profits = []
        N = len(profits)
        for i in range(N):
            best_profits.append((capital[i], -profits[i]))
        best_profits.sort()


# leetcode submit region end(Prohibit modification and deletion)


class Ipo(Solution):
    pass
