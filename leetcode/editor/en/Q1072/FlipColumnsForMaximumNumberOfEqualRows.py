from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row_sum = {}
        N = len(matrix)
        M = len(matrix[0])
        for i in range(N):
            row_sum[i] = sum(matrix[i])
        cache = {}
        def go(col, flip):
            if col == M:
                ans = 0
                for i in range(N):
                    if row_sum[i] == M or row_sum[i] == 0:
                       ans += 1
                return ans

            cache_key = ("".join(str(x) for x in matrix[0][:col+1]), col, flip)
            if cache_key in cache:
                return cache[cache_key]
            ans = 0
            if flip:
                for i in range(N):
                    row_sum[i] -= matrix[i][col]
                    matrix[i][col] = (matrix[i][col] + 1) % 2
                    row_sum[i] += matrix[i][col]
                ans = max(go(col + 1, True), go(col+1, False))
                for i in range(N):
                    row_sum[i] -= matrix[i][col]
                    matrix[i][col] = (matrix[i][col] + 1) % 2
                    row_sum[i] += matrix[i][col]
            else:
                ans = max(go(col + 1, True), go(col + 1, False))
            cache[cache_key] = ans
            return ans

        return max(go(0, True), go(0, False))
# leetcode submit region end(Prohibit modification and deletion)


class FlipColumnsForMaximumNumberOfEqualRows(Solution):
    pass
    