from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        N = len(mat)
        M = len(mat[0])
        rows = [0] * N
        cols = [0] * M
        pos = {}
        for i in range(N):
            for j in range(M):
                pos[mat[i][j]] = (i, j)
        rounds = 0
        for v in arr:

            i, j = pos[v]
            rows[i] += 1
            cols[j] += 1
            if rows[i] == N or cols[j] == M:
                return rounds
            rounds += 1
        return rounds


# leetcode submit region end(Prohibit modification and deletion)


class FirstCompletelyPaintedRowOrColumn(Solution):
    pass
