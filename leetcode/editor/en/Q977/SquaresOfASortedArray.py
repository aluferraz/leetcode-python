from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x ** 2 for x in nums])
# leetcode submit region end(Prohibit modification and deletion)


class SquaresOfASortedArray(Solution):
    pass