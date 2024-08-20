from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        M = len(points[0])

        for i in range(1, N):
            # Left-to-right pass
            left_dp = [0] * M
            left_dp[0] = points[i - 1][0]
            for j in range(1, M):
                left_dp[j] = max(left_dp[j - 1] - 1, points[i - 1][j])

            # Right-to-left pass
            right_dp = [0] * M
            right_dp[M - 1] = points[i - 1][M - 1]
            for j in range(M - 2, -1, -1):
                right_dp[j] = max(right_dp[j + 1] - 1, points[i - 1][j])

            # Update the current row based on max of left_dp and right_dp
            for j in range(M):
                points[i][j] += max(left_dp[j], right_dp[j])

        return max(points[-1])


# leetcode submit region end(Prohibit modification and deletion)


class MaximumNumberOfPointsWithCost(Solution):
    pass
