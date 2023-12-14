from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        N = len(mat)
        M = len(mat[0])
        rows = [0] * N
        cols = [0] * M

        for i in range(N):
            for j in range(M):
                rows[i] += mat[i][j]
                cols[j] += mat[i][j]
        ans = 0
        for i in range(N):
            for j in range(M):
                if rows[i] == 1 and cols[j] == 1 and mat[i][j] == 1:
                    ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SpecialPositionsInABinaryMatrix(Solution):
    pass
