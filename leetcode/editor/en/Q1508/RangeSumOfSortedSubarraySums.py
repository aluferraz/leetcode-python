from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        N = len(nums)
        all_subarrays = []
        for i in range(N):
            start = 0
            for j in range(i, N):
                start += nums[j]
                all_subarrays.append(start)
        M = len(all_subarrays)
        all_subarrays.sort()
        presum = [0] * M
        presum[0] = all_subarrays[0]
        for i in range(1, M):
            presum[i] = presum[i - 1] + all_subarrays[i]
        left -= 1
        right -= 1
        return presum[right] - (presum[left - 1] if left > 0 else 0)


# leetcode submit region end(Prohibit modification and deletion)


class RangeSumOfSortedSubarraySums(Solution):
    pass
