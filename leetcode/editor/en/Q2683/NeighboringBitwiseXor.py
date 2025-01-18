from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        N = len(derived)

        @cache
        def go(i, must_be):
            if i == N:
                return derived[0] == must_be
            if derived[i] == 1:
                if must_be == 0:
                    return go(i + 1, 1)
                else:
                    return go(i + 1, 0)

            if must_be == 0:
                return go(i + 1, 0)
            return go(i + 1, 1)

        return go(0, derived[0])


# leetcode submit region end(Prohibit modification and deletion)


class NeighboringBitwiseXor(Solution):
    pass
