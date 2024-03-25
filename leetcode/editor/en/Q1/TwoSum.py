from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            n = nums[i]
            if (target - n) in seen:
                return [seen[(target - n)], i]
            seen[n] = i
        return []
# leetcode submit region end(Prohibit modification and deletion)


class TwoSum(Solution):
    pass