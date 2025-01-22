from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        INF = 10 ** 20

        presum_1 = [0] * N
        presum_2 = [0] * N
        presum_1[0] = grid[0][0]
        presum_2[0] = grid[1][0]
        for i in range(1, N):
            presum_1[i] = presum_1[i - 1] + grid[0][i]
            presum_2[i] = presum_2[i - 1] + grid[1][i]
        best = INF
        for j in range(N):
            # if i go down here:
            ans1 = presum_1[j] + (presum_2[-1] - (presum_2[j - 1] if j > 0 else 0))
            ans2 = max((presum_2[j - 1] if j > 0 else 0), presum_1[-1] - presum_1[j])
            best = min(best, ans2)
        return best


# leetcode submit region end(Prohibit modification and deletion)


class GridGame(Solution):
    pass
