from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 1
        for i in range(N):
            while nums[i] > 0 and nums[i] < N and (nums[i] - 1) != i:
                if  nums[(nums[i] - 1)] == nums[i]:
                    break
                temp = nums[(nums[i] - 1)]
                nums[(nums[i] - 1)] = nums[i]
                nums[i] = temp
        for i in range(N):
            if nums[i] == ans:
                ans += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)


class FirstMissingPositive(Solution):
    pass