import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        if poured == 0:
            return 0
        if query_row == 0:
            return min(1, poured)

        def pascals(previous, row):
            next_row = [0] * (row + 1)
            for i in range(row + 1):
                if i - 1 >= 0:
                    next_row[i] += max(previous[i - 1] / 2, 0)
                if i < len(previous):
                    next_row[i] += max(previous[i] / 2, 0)
                if row == query_row and i == query_glass:
                    return max(next_row[query_glass], 0)
                next_row[i] = max(next_row[i] - 1, 0)
            return pascals(next_row, row + 1)

        return min(pascals([poured - 1], 1), 1)


# leetcode submit region end(Prohibit modification and deletion)


class ChampagneTower(Solution):
    pass
