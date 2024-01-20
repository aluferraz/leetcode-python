import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:


        N = len(matrix)
        M = len(matrix[0])
        INF = 10**20
        ans_matrix = [[INF for _ in range(M)] for _ in range(N)]
        for j in range(M):
            ans_matrix[0][j] = matrix[0][j]

        def isValidIdx(i,j):
            return i >= 0 and i < N and j >= 0 and j < M

        DIRECTIONS = [
            (1,-1),
            (1,0),
            (1,1),
        ]

        for i in range(N):
            for j in range(M):
                for u,v in DIRECTIONS:
                    if isValidIdx(i+u,j+v):
                        ans_matrix[i+u][j+v] = min(ans_matrix[i+u][j+v],
                                                   matrix[i+u][j+v] + ans_matrix[i][j]
                                                   )

        return min(ans_matrix[-1])






        
# leetcode submit region end(Prohibit modification and deletion)


class MinimumFallingPathSum(Solution):
    pass