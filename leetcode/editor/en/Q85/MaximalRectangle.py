from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        M = len(matrix[0])
        zeros_pos = [[] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 0:
                    zeros_pos[i].append(j)

        presum_mat = [[0 for _ in range(M)] for _ in range(N)]
        presum_mat[0][0] = matrix[0][0]
        for i in range(1, M):
            presum_mat[0][i] = presum_mat[0][i - 1] + matrix[0][i]
        for i in range(1, N):
            presum_mat[i][0] = presum_mat[i - 1][0] + matrix[i][0]

        for i in range(1, N):
            for j in range(1, M):
                presum_mat[i][j] = presum_mat[i - 1][j] + \
                                   presum_mat[i][j - 1] + \
                                   matrix[i][j] - \
                                   presum_mat[i - 1][j - 1]

        def valid_rectangle(start_i, start_j, i, j):
            if i >= N or j >= M:
                return 0
            remove_row = presum_mat[start_i - 1][j] if start_i > 0 else 0
            remove_col = presum_mat[i][start_j - 1] if start_j > 0 else 0
            readd = presum_mat[start_i - 1][start_j - 1] if start_i > 0 and start_j > 0 else 0
            total_here = presum_mat[i][j] - remove_col - remove_row + readd
            height = i - start_i + 1
            width = j - start_j + 1
            must_be = height * width
            if total_here != must_be:
                return 0
            return total_here

        def find_start(row, col):
            left = 0
            right = len(zeros_pos[row])
            ans = -1
            while left < right:
                mid = (left + right) // 2
                if zeros_pos[row][mid] >= col:
                    right = mid
                else:
                    ans = mid
                    left = mid + 1
            return ans

        ans = 0
        for i in range(N):
            for j in range(M):
                start_col = 0
                for k in range(i, -1, -1):
                    if matrix[k][j] == 0:
                        break
                    start_col_idx = find_start(k, j)
                    if len(zeros_pos[k]) > 0 and start_col_idx >= 0:
                        start_col = max(start_col, zeros_pos[k][start_col_idx] + 1)
                    ans = max(ans, valid_rectangle(k, start_col, i, j))

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MaximalRectangle(Solution):
    pass
