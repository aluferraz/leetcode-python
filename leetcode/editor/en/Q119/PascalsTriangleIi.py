from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        def pascals(row):
            if row == 0:
                return [1]
            N = row + 1
            prev = pascals(row - 1)
            current = [1] * N
            for i in range(1, N - 1):
                current[i] = prev[i] + prev[i - 1]
            return current

        return pascals(rowIndex)


# leetcode submit region end(Prohibit modification and deletion)


class PascalsTriangleIi(Solution):
    pass
