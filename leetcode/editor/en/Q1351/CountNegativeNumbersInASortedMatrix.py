# leetcode submit region begin(Prohibit modification and deletion)

ROW_DIR = 0
COL_DIR = 1


class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        N = len(grid)
        M = len(grid[0])

        def binarySearch(pos, target):
            left = 0
            right = M

            while left < right:
                mid = (left + right) // 2
                if grid[pos][mid] > target:
                    left = mid + 1
                else:
                    right = mid
            return left

        ans = 0
        for i in range(N):
            negCol = binarySearch(i, -1)
            ans += M - negCol
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class CountNegativeNumbersInASortedMatrix(Solution):
    pass
