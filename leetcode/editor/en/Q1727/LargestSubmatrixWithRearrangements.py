import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        N = len(matrix)
        M = len(matrix[0])
        if N == 1:
            return sum(matrix[0])

        def col_score(j):
            score = 0

            for i in range(N):
                score += (matrix[i][j] ** (N - i))
            return score

        scores = []
        for j in range(M):
            scores.append((col_score(j), j))
        scores.sort(reverse=True)
        ans = scores[0][0]
        new_matrix = [[-1 for _ in range(M)] for _ in range(N)]
        new_matrix_idx = 0
        for _, col in scores:
            for i in range(N):
                new_matrix[i][new_matrix_idx] = matrix[i][col]
            new_matrix_idx += 1

        for j in range(M):
            if new_matrix[0][j] == 0 or new_matrix[-1][j] == 0:
                break
            ans = max(ans, N * (j + 1))

        return max(ans, self.largestSubmatrix(new_matrix[1::]))
        # leetcode submit region end(Prohibit modification and deletion)


class LargestSubmatrixWithRearrangements(Solution):
    pass
