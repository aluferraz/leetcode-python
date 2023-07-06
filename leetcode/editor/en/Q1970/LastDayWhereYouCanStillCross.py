import collections
from cmath import sqrt
from functools import cache
from typing import List
import sortedcollections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        WATER = 1
        LAND = 0
        matrix = [[LAND for _ in range(col)] for _ in range(row)]
        parents = [-1 for _ in range(row * col)]
        transversePath = [0 for _ in range(row * col)]
        N = len(cells)
        ans = 0
        for i in range(N):
            (waterRow, waterCol) = cells[i]
            cells[i] = [waterRow - 1, waterCol - 1]

        def isValidIdx(i, j):
            return i >= 0 and i < row and j >= 0 and j < col

        coordsMap = {}
        coordIdx = 0
        for i in range(row):
            for j in range(col):
                coordsMap[(i, j)] = coordIdx
                coordIdx += 1

        def union(i, j):
            if i == j:
                return
            if parents[j] < parents[i]:
                return union(j, i)

            parents[i] += parents[j]
            parents[j] = i
            transversePath[i] |= transversePath[j]

        def find(i):
            while parents[i] >= 0:
                i = parents[i]
            return i

        def go(i, j):
            corners = 0
            if i == 0:
                corners |= 1  # UP
            if j == 0:
                corners |= (1 << 1)  # LEFT
            if j == col - 1:
                corners |= (1 << 2)  # RIGHT
            if i == row - 1:
                corners |= (1 << 3)  # BOTTOM
            transversePath[coordsMap[(i, j)]] |= corners

            if isValidIdx(i + 1, j) and matrix[i + 1][j]:
                union(find(coordsMap[(i + 1, j)]), find(coordsMap[(i, j)]))
            if isValidIdx(i - 1, j) and matrix[i - 1][j]:
                union(find(coordsMap[(i - 1, j)]), find(coordsMap[(i, j)]))
            if isValidIdx(i, j + 1) and matrix[i][j + 1]:
                union(find(coordsMap[(i, j + 1)]), find(coordsMap[(i, j)]))
            if isValidIdx(i, j - 1) and matrix[i][j - 1]:
                union(find(coordsMap[(i, j - 1)]), find(coordsMap[(i, j)]))
            if isValidIdx(i - 1, j - 1) and matrix[i - 1][j - 1]:
                union(find(coordsMap[(i - 1, j - 1)]), find(coordsMap[(i, j)]))
            if isValidIdx(i - 1, j + 1) and matrix[i - 1][j + 1]:
                union(find(coordsMap[(i - 1, j + 1)]), find(coordsMap[(i, j)]))
            if isValidIdx(i + 1, j - 1) and matrix[i + 1][j - 1]:
                union(find(coordsMap[(i + 1, j - 1)]), find(coordsMap[(i, j)]))
            if isValidIdx(i + 1, j + 1) and matrix[i + 1][j + 1]:
                union(find(coordsMap[(i + 1, j + 1)]), find(coordsMap[(i, j)]))

        for i in range(N):
            (waterRow, waterCol) = cells[i]
            if matrix[waterRow][waterCol] != LAND:
                continue
            matrix[waterRow][waterCol] = WATER
            go(waterRow, waterCol)

            corners = transversePath[find(coordsMap[(waterRow, waterCol)])]
            if corners & (1 << 1) != 0 and corners & (1 << 2) != 0:
                return ans
            ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LastDayWhereYouCanStillCross(Solution):
    pass
