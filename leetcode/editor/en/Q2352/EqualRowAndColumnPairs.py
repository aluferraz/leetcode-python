import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        N = len(grid)
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        for i in range(N):
            for j in range(N):
                rows[i].append(str(grid[i][j]))
                cols[j].append(str(grid[i][j]))

        rowsMap = collections.Counter()
        colsMap = collections.Counter()
        for row in rows:
            rowsMap[",".join(rows[row])] += 1
        for col in cols:
            colsMap[",".join(cols[col])] += 1
        ans = 0

        for r in rowsMap:
            if r in colsMap:
                ans += (rowsMap[r] * colsMap[r])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class EqualRowAndColumnPairs(Solution):
    pass
