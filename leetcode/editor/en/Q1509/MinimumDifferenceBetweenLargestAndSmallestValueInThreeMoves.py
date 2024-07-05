from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        INF = 10**20

        best = INF
        for i in range(N):
            left = 0
            right = N-1
            for _ in range(3):
                ldiff = -INF
                rdiff = -INF
                if left < i:
                    ldiff = nums[right] - nums[left + 1]
                if right > i:
                    rdiff = nums[right - 1] - nums[left]
                if ldiff >= rdiff and left < i:
                    left += 1
                elif right > i:
                    right -= 1
                best = min(best, nums[right] - nums[left])
        return best


# leetcode submit region end(Prohibit modification and deletion)


class MinimumDifferenceBetweenLargestAndSmallestValueInThreeMoves(Solution):
    pass
    