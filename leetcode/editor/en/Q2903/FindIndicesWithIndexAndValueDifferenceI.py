from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        N = len(nums)
        for i in range(0, N - indexDifference):
            for j in range(i + indexDifference, N):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]


# leetcode submit region end(Prohibit modification and deletion)


class FindIndicesWithIndexAndValueDifferenceI(Solution):
    pass
