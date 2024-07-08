from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        logN = N.bit_length()
        maxs = [[0 for _ in range(logN)] for _ in range(N)]
        mins = [[0 for _ in range(logN)] for _ in range(N)]
        for i in range(N):
            maxs[i][0] = nums[i]
            mins[i][0] = nums[i]
        for j in range(1, logN):
            for i in range(N - (1 << j) + 1):
                maxs[i][j] = max(maxs[i][j - 1], maxs[i + (1 << (j - 1))][j - 1])
                mins[i][j] = min(mins[i][j - 1], mins[i + (1 << (j - 1))][j - 1])

        def get_min(left, right):
            logRange = (right - left + 1).bit_length() - 1  # Precalculate log
            start = right - (1 << logRange) + 1
            return min(mins[left][logRange], mins[start][logRange])

        def get_max(left, right):
            logRange = (right - left + 1).bit_length() - 1  # Precalculate log
            start = right - (1 << logRange) + 1
            return max(maxs[left][logRange], maxs[start][logRange])

        def good(size):
            for i in range(N - size + 1):
                min_in_range = get_min(i, i + size - 1)
                max_in_range = get_max(i, i + size - 1)
                if abs(max_in_range - min_in_range) <= limit:
                    return True
            return False

        left = 0
        right = N + 1
        ans = 0
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LongestContinuousSubarrayWithAbsoluteDiffLessThanOrEqualToLimit(Solution):
    pass
