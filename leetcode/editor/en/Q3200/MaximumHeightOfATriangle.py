from functools import cache
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        @cache
        def go(current_round, red_balls, blue_balls, row):
            if current_round == 0 and red_balls < row:
                return 0
            elif current_round == 1 and blue_balls < row:
                return 0
            next_round = ((current_round + 1) % 2)
            if next_round == 1:
                return 1 + go(next_round, red_balls - row, blue_balls, row + 1)
            return 1 + go(next_round, red_balls, blue_balls - row, row + 1)

        return max(go(0, red, blue, 1), go(1, red, blue, 1))
# leetcode submit region end(Prohibit modification and deletion)


class MaximumHeightOfATriangle(Solution):
    pass
    