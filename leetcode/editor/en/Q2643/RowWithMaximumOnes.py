from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        max_ones = 0
        max_row = 0
        N = len(mat)
        for i in range(N):
            row = mat[i]
            total_ones = sum(row)
            if total_ones > max_ones:
                max_ones = total_ones
                max_row = i
        return [max_row, max_ones]

        # leetcode submit region end(Prohibit modification and deletion)


class RowWithMaximumOnes(Solution):
    pass
