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

        def is_valid(i, j):
            return i >= 0 and i < N and j >= 0 and j < M

        seen = set()
        ans = []

        def solve(i, j, flip, ans_here):
            if not is_valid(i, j):
                if flip:
                    ans_here.reverse()
                return ans
            seen.add((i,j))
            ans_here.append(mat[i][j])
            return solve(i + 1, j - 1, flip, ans_here)

        cur_flip = True

        for i in range(N):
            for j in range(M):
                if (i, j) in seen:
                    continue
                ans_here = []
                solve(i, j, cur_flip, ans_here)
                cur_flip = not cur_flip
                for el in ans_here:
                    ans.append(el)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class DiagonalTraverse(Solution):
    pass
