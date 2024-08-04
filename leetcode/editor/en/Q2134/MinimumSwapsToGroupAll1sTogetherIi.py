from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        N = len(nums)
        right = 0
        window_ones = 0
        best = N
        while right < (N * 2):
            if nums[right % N] == 1:
                window_ones += 1
            if (right + 1) < ones:
                right += 1
                continue
            if (right + 1) > ones:
                if nums[(right - ones) % N] == 1:
                    window_ones -= 1
            best = min(best, ones - window_ones)
            right += 1
        return best


# leetcode submit region end(Prohibit modification and deletion)


class MinimumSwapsToGroupAll1sTogetherIi(Solution):
    pass
