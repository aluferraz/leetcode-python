from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        N = len(matrix)

        row_elements = [0] * N
        col_elements = [0] * N

        for i in range(N):
            for j in range(N):
                el = matrix[i][j]
                if el < 0 or el > N:
                    return False
                if row_elements[i] & (1 << el) == 0:
                    row_elements[i] |= (1 << el)
                else:
                    return False
                if col_elements[j] & (1 << el) == 0:
                    col_elements[j] |= (1 << el)
                else:
                    return False
        target = 0
        for i in range(1, N + 1):
            target |= (1 << i)
        for i in range(N):
            if row_elements[i] != target or col_elements[i] != target:
                return False

        return True


# leetcode submit region end(Prohibit modification and deletion)


class CheckIfEveryRowAndColumnContainsAllNumbers(Solution):
    pass
