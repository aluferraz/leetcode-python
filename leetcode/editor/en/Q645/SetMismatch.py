from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        seen = set()
        tracked = None
        for i in range(len(nums)):
            if nums[i] in seen:
                ans.append(nums[i])
            seen.add(nums[i])
        for i in range(1, len(nums)+1):
            if i not in seen:
                ans.append(i)
                break
        return ans
# leetcode submit region end(Prohibit modification and deletion)


class SetMismatch(Solution):
    pass