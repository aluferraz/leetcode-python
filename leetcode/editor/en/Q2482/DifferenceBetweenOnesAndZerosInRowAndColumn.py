from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(grid)
        M = len(grid[0])
        ones_row = [0] * N
        ones_col = [0] * M
        ans = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                ones_row[i] += grid[i][j]
                ones_col[j] += grid[i][j]

        for i in range(N):
            for j in range(M):
                zeros_row = N - ones_row[i]
                zeros_col = M - ones_col[j]
                ans[i][j] = ones_row[i] + ones_col[j] - zeros_row - zeros_col
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class DifferenceBetweenOnesAndZerosInRowAndColumn(Solution):
    pass
