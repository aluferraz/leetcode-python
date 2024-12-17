import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        N = len(quantities)
        left = 1
        right = max(quantities)

        def go(limit, stores, i):
            if i == N:
                return stores >= 0
            to_consume = math.ceil(quantities[i] / limit)
            return go(limit, stores - to_consume, i + 1)

        def good(upper):
            return go(upper, n, 0)

        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1

        return left


# leetcode submit region end(Prohibit modification and deletion)


class MinimizedMaximumOfProductsDistributedToAnyStore(Solution):
    pass
