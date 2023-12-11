from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(matrix)
        M = len(matrix[0])
        ans = [[0 for _ in range(N)] for _ in range(M)]

        for i in range(N):
            for j in range(M):
                ans[j][i] = matrix[i][j]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class TransposeMatrix(Solution):
    pass
