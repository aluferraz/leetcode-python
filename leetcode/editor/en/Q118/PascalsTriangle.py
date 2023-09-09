from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = []
        if numRows == 0:
            return ans
        ans.append([1])
        if numRows == 1:
            return ans
        ans.append([1, 1])
        if numRows == 2:
            return ans

        def go(i):
            if i == numRows:
                return
            prev = ans[i - 1]
            N = len(prev)
            row = [1] * (N + 1)
            for j in range(1, N):
                row[j] = prev[j - 1] + prev[j]
            ans.append(row)
            go(i + 1)

        go(2)
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)


class PascalsTriangle(Solution):
    pass
    