import collections
from typing import List

import sortedcontainers


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        freq_counter = collections.defaultdict(int)
        max_freq = sortedcontainers.SortedList()
        left = 0
        right = 0
        ans = 0
        while right < N:
            max_freq.discard(freq_counter[nums[right]])
            freq_counter[nums[right]] += 1
            max_freq.add(freq_counter[nums[right]])
            while left < right and max_freq[-1] > k:
                max_freq.discard(freq_counter[nums[left]])
                freq_counter[nums[left]] -= 1
                max_freq.add(freq_counter[nums[left]])
                left += 1
            if max_freq[-1] <= k:
                ans = max(ans, right - left + 1)
            right += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LengthOfLongestSubarrayWithAtMostKFrequency(Solution):
    pass
