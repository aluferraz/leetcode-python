import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        target = max(nums) #O(N)
        N = len(nums)
        ans = 0
        target_idxes = collections.deque()
        started_at = 0
        while right < N:
            if nums[right] == target:
                target_idxes.append(right)
            if len(target_idxes) == k:
                ans += self.number_of_subarray(target_idxes[0] - started_at, right, N)
                started_at = target_idxes.popleft() + 1
            right += 1
        return ans
    def number_of_subarray(self, first_saw, right, N):
        left_freedom = first_saw + 1  # 0 indexed
        right_freedom = N - right
        return left_freedom * right_freedom
# leetcode submit region end(Prohibit modification and deletion)


class CountSubarraysWhereMaxElementAppearsAtLeastKTimes(Solution):
    pass