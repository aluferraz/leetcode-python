import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        N = len(nums)
        diagonals = collections.defaultdict(list)
        ans = []
        for i in range(N):
            for j in range(len(nums[i])):
                diagonals[(i + j)].append((i, j))
        for k, l in diagonals.items():
            i, j = l[0]
            u, v = l[-1]
            # if i == v and j == u:
            for f in range(len(l) - 1, -1, -1):
                (i, j) = l[f]
                ans.append(nums[i][j])
        return ans

        def find_next(start, row, col):

            left = start
            right = row
            found_at = -1

            if row > 0 and len(nums[row - 1]) > col + 1:
                return row - 1

            while left < right:
                mid = (left + right) // 2
                target = col + (row - mid)
                if len(nums[mid]) > target:
                    found_at = mid
                    left = mid + 1
                else:
                    return max(find_next(start, mid, target), find_next(mid + 1, row, col))

            return found_at

        def go(i, j):
            if i < 0:
                return

            # ans.append(nums[i][j])
            ans.append((i, j))

            nums[i][j] *= -1
            next_row = find_next(0, i, j)
            next_col = j + (i - next_row)

            return go(next_row, next_col)

        start_row = 0
        for i in range(len(nums)):
            go(i, 0)
            print(ans)
            ans = []
            if nums[i][-1] >= 0:
                start_row = max(start_row, i)

        def binSearch(arr):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= 0:
                    right = mid
                else:
                    left = mid + 1
            return left

        for i in range(len(nums) - 1, -1, -1):
            startCol = binSearch(nums[i])
            for j in range(startCol, len(nums[i])):
                if nums[i][j] >= 0:
                    go(i, j)
                    print(ans)
                    ans = []

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class DiagonalTraverseIi(Solution):
    pass
