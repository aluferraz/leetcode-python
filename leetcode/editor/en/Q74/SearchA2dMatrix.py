from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        N = len(matrix)
        M = len(matrix[0])

        def bin_search_col(j):
            left = 0
            right = M - 1
            closest = 0
            while left <= right:
                mid = (left + right) // 2
                if matrix[j][mid] == target:
                    return mid
                elif matrix[j][mid] < target:
                    closest = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return closest

        def bin_search_row(i):
            left = 0
            right = N - 1
            closest = 0
            while left <= right:
                mid = (left + right) // 2
                if matrix[mid][i] == target:
                    return mid
                elif matrix[mid][i] < target:
                    closest = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return closest

        srow = 0
        erow = bin_search_row(0)

        while srow <= erow:
            mid = (srow + erow) // 2
            col = bin_search_col(mid)
            if matrix[mid][col] == target:
                return True
            elif matrix[mid][col] < target:
                srow = mid + 1
            else:
                erow = mid - 1
        return False


# leetcode submit region end(Prohibit modification and deletion)


class SearchA2dMatrix(Solution):
    pass
