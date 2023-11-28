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
        for i in range(1, N):
            for j in range(M):
                matrix[i][j] += matrix[i - 1][j]
        

# leetcode submit region end(Prohibit modification and deletion)


class LargestSubmatrixWithRearrangements(Solution):
    pass
