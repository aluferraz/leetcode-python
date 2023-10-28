from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        INF = 10 ** 20
        N = len(nums)
        max_ahead = [N - 1] * N
        min_ahead = [N - 1] * N
        for i in range(N - 2, -1, -1):
            max_ahead[i] = max_ahead[i+1]
            min_ahead[i] = min_ahead[i+1]
            if nums[i] >= nums[max_ahead[i + 1]]:
                max_ahead[i] = i
            if nums[i] <= nums[min_ahead[i + 1]]:
                min_ahead[i] = i

        for i in range(0, N - indexDifference):

            if abs(nums[i] - nums[max_ahead[i + indexDifference]]) >= valueDifference:
                return [i, max_ahead[i + indexDifference]]
            if abs(nums[i] - nums[min_ahead[i + indexDifference]]) >= valueDifference:
                return [i, min_ahead[i + indexDifference]]
        return [-1, -1]


# leetcode submit region end(Prohibit modification and deletion)


class FindIndicesWithIndexAndValueDifferenceIi(Solution):
    pass
