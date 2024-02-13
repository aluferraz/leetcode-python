from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = 0
        N = len(nums)
        while left < N:
            while right < N and nums[left] == nums[right]:
                right += 1
            if right - left + 1 > N // 2:
                return nums[left]
            left = right
            left += 1

        return -1
        
# leetcode submit region end(Prohibit modification and deletion)


class MajorityElement(Solution):
    pass