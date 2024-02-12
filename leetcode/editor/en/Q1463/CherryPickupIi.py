from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        cache = {}
        def pick(r1, r2):
            y, x = r1
            if y == N or x < 0 or x >= M:
                return 0
            value = grid[y][x]
            if (value, r1,r2) in cache:
                return cache[(value, r1,r2)]
            grid[y][x] = 0
            ans = value + pick(r2, (y + 1, x))
            ans = max(ans, value + pick(r2, (y + 1, x - 1)))
            ans = max(ans, value + pick(r2, (y + 1, x + 1)))
            grid[y][x] = value
            cache[(value, r1, r2)] = ans
            return ans

        return pick((0, 0), (0, M - 1))
    # leetcode submit region end(Prohibit modification and deletion)


class CherryPickupIi(Solution):
    pass
