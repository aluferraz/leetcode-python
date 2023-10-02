from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
import sortedcontainers


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        N = len(nums)
        INF = 10 ** 20
        min_until = [INF] * N
        min_until[0] = nums[0]

        for i in range(1, N):
            min_until[i] = min(min_until[i - 1], nums[i])

        seen = sortedcontainers.SortedList()

        def bin_s(target):
            left = 0
            right = len(seen) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if seen[mid] < target:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        for i in range(N - 1, 0, -1):
            if min_until[i - 1] < nums[i]:
                max_threshold = bin_s(nums[i])
                if max_threshold >= 0 and seen[max_threshold] > min_until[i - 1]:
                    return True
            seen.add(nums[i])
        return False


# leetcode submit region end(Prohibit modification and deletion)


class One32Pattern(Solution):
    pass
