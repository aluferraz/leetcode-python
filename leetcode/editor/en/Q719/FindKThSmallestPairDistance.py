from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()

        def good(target):
            count = 0
            right = 0
            for left in range(N):
                while right < N and nums[right] - nums[left] <= target:
                    right += 1
                count += (right - left - 1)
            return count >= k

        left = 0
        right = nums[-1]
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left


# leetcode submit region end(Prohibit modification and deletion)


class FindKThSmallestPairDistance(Solution):
    pass
