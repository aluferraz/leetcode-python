from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        max_reachable = 0  # Track the largest number reachable
        patches = 0
        i = 0

        while max_reachable < n:
            if i < len(nums) and nums[i] <= max_reachable + 1:
                max_reachable += nums[i]  # Extend reachable range
                i += 1
            else:
                max_reachable += max_reachable + 1  # Add a patch (the next missing number)
                patches += 1

        return patches


# leetcode submit region end(Prohibit modification and deletion)


class PatchingArray(Solution):
    pass
