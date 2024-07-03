from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        N = len(mat)
        M = len(mat[0])
        ans = []

        def go(i, j, d):
            if i == N - 1 and j == M - 1:
                return
            if i < 0 or j >= M:
                return go(i + 1, j + 1, (d + 1) % 2)
            if j < 0 or i >= N:
                return go(i + 1, 0, (d + 1) % 2)
            ans.append(mat[i][j])
            if d == 0:

                
                return go(i - 1, j + 1, d)
            return go(i + 1, j - 1, d)
        go(0,0,0)
        return ans

# leetcode submit region end(Prohibit modification and deletion)


class DiagonalTraverse(Solution):
    pass
