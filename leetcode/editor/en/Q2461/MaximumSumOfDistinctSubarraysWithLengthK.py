import sortedcontainers

import collections
import heapq
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = collections.defaultdict(int)
        window = collections.deque()
        wsum = 0
        N = len(nums)
        ans = 0
        for i in range(N):
            window.append(nums[i])
            counter[nums[i]] += 1
            wsum += nums[i]
            if len(window) < k:
                continue
            if len(window) > k:
                to_remove = window.popleft()
                counter[to_remove] -= 1
                if counter[to_remove] == 0:
                    counter.pop(to_remove)
                wsum -= to_remove
            if len(counter) == k:
                ans = max(ans, wsum)
        return ans


        
# leetcode submit region end(Prohibit modification and deletion)


class MaximumSumOfDistinctSubarraysWithLengthK(Solution):
    pass
    