import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        max_l = n
        min_r = 0
        if len(left) > 0:
            max_l = max(left)
        else:
            return n - min(right) if len(right) > 0 else 0
        if len(right) > 0:
            min_r = min(right)
        else:
            return max_l

        return max(n - min_r, max_l)


# leetcode submit region end(Prohibit modification and deletion)


class LastMomentBeforeAllAntsFallOutOfAPlank(Solution):
    pass
