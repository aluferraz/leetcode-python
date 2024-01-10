# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def get(self, row: int, col: int) -> int:
        pass

    def dimensions(self) -> list:
        pass


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        R, C = binaryMatrix.dimensions()
        ans = R
        for i in range(R):
            left = 0
            right = R
            while left < right:
                mid = (left + right) // 2
                if binaryMatrix.get(i,mid) == 0:
                    left = mid + 1
                else:
                    right = mid
            ans = min(ans, left)
        return ans if ans < R else -1




        # leetcode submit region end(Prohibit modification and deletion)


class LeftmostColumnWithAtLeastAOne(Solution):
    pass
