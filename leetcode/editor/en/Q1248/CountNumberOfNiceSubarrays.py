from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        ans = 0
        odds = 0
        N = len(nums)
        extra_aft = 0
        extra_bef = 0
        while right < N:
            odds += (nums[right] % 2)
            while left < right and (nums[left] % 2) == 0:
                extra_bef += 1
                left += 1
            if odds == k:
                extra_aft += 1
            if odds > k:
                ans += ((extra_bef + 1) * extra_aft)
                extra_bef = 0
                extra_aft = 1
            while odds > k:
                odds -= (nums[left] % 2)
                left += 1
            right += 1
        while left < right and (nums[left] % 2) == 0:
            extra_bef += 1
            left += 1
        if odds == k:
            ans += ((extra_bef + 1) * extra_aft)

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class CountNumberOfNiceSubarrays(Solution):
    pass
