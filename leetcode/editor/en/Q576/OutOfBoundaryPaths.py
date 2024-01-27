# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        cache = [[[0 for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]
        has_cache = [[[False for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]
        MOD = 10 ** 9 + 7

        def go(i, j, moves):
            if moves > maxMove:
                return 0
            if i >= m or i < 0 or j >= n or j < 0:
                return 1
            if has_cache[i][j][moves]:
                return cache[i][j][moves]
            ans = 0
            ans = (ans + go(i + 1, j, moves + 1)) % MOD
            ans = (ans + go(i - 1, j, moves + 1)) % MOD
            ans = (ans + go(i, j - 1, moves + 1)) % MOD
            ans = (ans + go(i, j + 1, moves + 1)) % MOD
            cache[i][j][moves] = ans

            has_cache[i][j][moves] = True
            return ans

        return go(startRow, startColumn, 0) % MOD


# leetcode submit region end(Prohibit modification and deletion)


class OutOfBoundaryPaths(Solution):
    pass
