from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        N = len(nums)
        ans = 0
        prefix_counter = [0] * N
        suffix_counter = [0] * N
        window_counter = 0
        for i in range(N):
            prefix_counter[i] = window_counter
            if nums[i] == 1:
                if goal == 0:
                    ans += (window_counter * (window_counter + 1)) // 2
                window_counter = 0
            else:
                window_counter += 1
        prefix_counter[-1] = window_counter
        if goal == 0:
            ans += (window_counter * (window_counter + 1)) // 2
            return ans

        window_counter = 0
        for i in range(N - 1, -1, -1):
            suffix_counter[i] = window_counter
            if nums[i] == 1:
                window_counter = 0
            else:
                window_counter += 1
        if nums[0] == 0:
            suffix_counter[0] = window_counter
        left = 0

        while left < N:
            while left < N - 1 and nums[left] == 0:
                left += 1
            window_counter = nums[left]
            right = left + 1
            while right < N and window_counter < goal:
                window_counter += nums[right]
                right += 1
            if window_counter == goal:
                ans += 1 * (prefix_counter[left] + 1) * (suffix_counter[right - 1] + 1)
            left += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)


class BinarySubarraysWithSum(Solution):
    pass
