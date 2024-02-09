import math
from functools import cache
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1, n+1):
            sqr = math.sqrt(i)

            if sqr == int(sqr):
                squares.append(i)

        INF = 10 ** 20
        @cache
        def go(num):
            if num == 0:
                return 0
            if num < 0:
                return INF
            ans = INF
            for i in range(len(squares) - 1, -1, -1):
                ans = min(ans, 1 + go(num - squares[i]))
            return ans


        return go(n)
# leetcode submit region end(Prohibit modification and deletion)


class PerfectSquares(Solution):
    pass