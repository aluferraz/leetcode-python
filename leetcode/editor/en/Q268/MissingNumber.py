from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
# leetcode submit region end(Prohibit modification and deletion)


class MissingNumber(Solution):
    pass