from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = -10**20
        N = len(nums)
        left = 0
        right = N-1
        while left < right:
            ans = max(ans,nums[left] + nums[right])
            left += 1
            right -= 1
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)


class MinimizeMaximumPairSumInArray(Solution):
    pass
    