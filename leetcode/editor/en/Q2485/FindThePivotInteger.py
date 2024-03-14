from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pivotInteger(self, n: int) -> int:
        def natural_sum(k):
            if k == 0:
                return 0
            return (k * (k + 1)) // 2


        for i in range(n + 1):
            if natural_sum(i) == natural_sum(n) - natural_sum(i-1):
                return i
        return -1

# leetcode submit region end(Prohibit modification and deletion)


class FindThePivotInteger(Solution):
    pass