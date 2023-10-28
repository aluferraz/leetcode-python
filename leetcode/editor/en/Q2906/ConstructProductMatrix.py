from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def constructProductMatrix(self, grid):
        """
        # :type grid: List[List[int]]
        # :rtype: List[List[int]]
        # """
        pass
        # total_prod = 1
        # N = len(grid)
        # M = len(grid[0])
        # zero_count = 0
        # zero_idx = [-1, -1]
        # for i in range(N):
        #     for j in range(M):
        #         if grid[i][j] % 12345 == 0:
        #             zero_count += 1
        #             zero_idx = [i, j]
        #         else:
        #             total_prod = total_prod * grid[i][j]
        # if zero_count > 1:
        #     return [[0 for _ in range(M)] for _ in range(N)]
        # if zero_count == 1:
        #     ans = [[0 for _ in range(M)] for _ in range(N)]
        #     ans[zero_idx[0]][zero_idx[1]] = total_prod
        #     return ans
        #
        # ans = [[total_prod for _ in range(M)] for _ in range(N)]
        # for i in range(N):
        #     for j in range(M):
        #         ans[i][j] //= (grid[i][j])
        #         ans[i][j] %= 12345
        # return ans


# leetcode submit region end(Prohibit modification and deletion)


class ConstructProductMatrix(Solution):
    pass
