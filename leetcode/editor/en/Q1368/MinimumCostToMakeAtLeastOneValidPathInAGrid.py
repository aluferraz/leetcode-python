from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        DIRECTIONS = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0),
        }

        N = len(grid)
        M = len(grid[0])

        def is_valid_idx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M

        def go(i, j, total_cost, flipped):
            if total_cost < 0:
                return False
            if i == N - 1 and j == M - 1:
                return True

            next_direction = grid[i][j]

            for d in range(1, 5):
                cost = 1 if d != next_direction else 0
                next_i, next_j = i + DIRECTIONS[d][0], j + DIRECTIONS[d][1]
                if not is_valid_idx(next_i, next_j):
                    continue
                if cost == 1:
                    flipped[i][j] += cost
                    if flipped[i][j] < 2:
                        if go(next_i, next_j, (total_cost - cost), flipped):
                            return True
                    flipped[i][j] -= cost
            return False

        def good(total_cost_allowed):
            return go(0, 0, total_cost_allowed, [[0 for _ in range(M)] for _ in range(N)])

        left = 0
        right = N * M + 1
        ans = 10 ** 20
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                ans = mid
                right = mid
            else:
                left = mid + 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumCostToMakeAtLeastOneValidPathInAGrid(Solution):
    pass
