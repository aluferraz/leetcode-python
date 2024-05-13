from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        M = len(grid[0])
        start = 0
        ans = []
        for i in range(N):
            row = []
            for j in range(M):
                if i + 2 >= N or j + 2 >= M:
                    continue
                max_local = -1
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        max_local = max(max_local, grid[k][l])
                row.append(max_local)
            if len(row) > 0:
                ans.append(row)

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LargestLocalValuesInAMatrix(Solution):
    pass
