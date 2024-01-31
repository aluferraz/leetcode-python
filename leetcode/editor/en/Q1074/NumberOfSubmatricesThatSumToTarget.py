from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        N = len(matrix)
        M = len(matrix[0])
        psum = [[0 for _ in range(M)] for _ in range(N)]
        psum[0][0] = matrix[0][0]
        for i in range(1, N):
            psum[i][0] = matrix[i][0] + psum[i - 1][0]
        for j in range(1, M):
            psum[0][j] = matrix[0][j] + psum[0][j - 1]

        for i in range(1, N):
            for j in range(1, M):
                psum[i][j] = (psum[i - 1][j] +
                              psum[i][j - 1]
                              - psum[i - 1][j - 1] + matrix[i][j])

        ans = 0

        def get_targets(start_row, start_col, cur_row, cur_col):
            if cur_row == N or cur_col == M:
                return 0
            prev = 0
            if start_row > 0 and start_col > 0:
                prev = psum[start_row - 1][M - 1] + \
                       psum[N - 1][start_col - 1]
            elif start_row > 0:
                prev = psum[start_row - 1][start_col]
            elif start_col > 0:
                prev = psum[start_row][start_col - 1]

            sum_here = psum[cur_row][cur_col] - prev
            tot_here = 0
            if sum_here == target:
                tot_here += 1
            tot_here += get_targets(start_row, start_col, cur_row + 1, cur_col)
            tot_here += get_targets(start_row, start_col, cur_row, cur_col + 1)
            return tot_here

        for i in range(N):
            for j in range(M):
                ans += get_targets(i, j, i, j)

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfSubmatricesThatSumToTarget(Solution):
    pass
