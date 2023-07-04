# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        directions = [
            (-1, -2),
            (-2, -1),
            (-1, 2),
            (-2, 1),
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
        ]

        def isValidIdx(r, c):
            return r >= 0 and r < n and c >= 0 and c < n

        cache = {}

        def count(r, c, k):
            if not isValidIdx(r, c):
                return 0
            if k == 0:
                return 1

            if (r, c, k) in cache:
                return cache[(r, c, k)]
            valid = 0
            ans = 0
            for yi, xi in directions:
                newRow, newCol = r + yi, c + xi
                if isValidIdx(newRow, newCol):
                    valid += 1
                    nextValidMoves = count(newRow, newCol, k - 1)
                    ans += (1 / 8) * nextValidMoves
            cache[(r, c, k)] = ans
            return ans

        return count(row, column, k)


# leetcode submit region end(Prohibit modification and deletion)


class KnightProbabilityInChessboard(Solution):
    pass
