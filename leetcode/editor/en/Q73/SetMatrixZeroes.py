from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])

        cols = set()
        rows = set()

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    cols.add(j)
                    rows.add(j)

        for i in range(M):
            if i in rows:
                matrix[i] = [0] * N
            else:
                for c in cols:
                    matrix[i][c] = 0



# leetcode submit region end(Prohibit modification and deletion)


class SetMatrixZeroes(Solution):
    pass
