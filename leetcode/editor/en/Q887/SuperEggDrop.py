from math import ceil, log, floor
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def superEggDrop(self, k: int, N: int) -> int:

        cache = {}

        def guess(left, right, eggs):
            if left > right:
                return 0
            if (left, right, eggs) in cache:
                return cache[(left, right)]
            size = right - left + 1
            if eggs == 1:
                return size
            if size == 1:
                return 1
            minimum = floor(log(size, 2)) + 1
            mid = (left + right) // 2
            if minimum == eggs:
                ans = minimum
            else:
                ans = 1 + max(guess(left, mid, eggs - 1), guess(mid + 1, right, eggs))
            cache[(left, right, eggs)] = ans
            return ans

        return guess(0, N, k)


# leetcode submit region end(Prohibit modification and deletion)


class SuperEggDrop(Solution):
    pass
