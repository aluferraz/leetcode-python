import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        """
        :type width: int
        :type height: int
        :type sideLength: int
        :type maxOnes: int
        :rtype: int
        """
        if maxOnes == 0:
            return 0
        matrix = [
            [0 for _ in range(sideLength)] for _ in range(sideLength)
        ]

        squares = {}

        def isValidIdx(row, col):
            return row >= 0 and row < height and col >= 0 and col < height

        for i in range(height):
            for j in range(width):
                matrix[i % sideLength][j % sideLength] += 1

        most_frequent = []
        for i in range(sideLength):
            for j in range(sideLength):
                heapq.heappush(most_frequent, ((-matrix[i][j], (i, j))))

        total = 0
        for i in range(maxOnes):
            total += abs(heapq.heappop(most_frequent)[0])
        return total



# leetcode submit region end(Prohibit modification and deletion)


class MaximumNumberOfOnes(Solution):
    pass
