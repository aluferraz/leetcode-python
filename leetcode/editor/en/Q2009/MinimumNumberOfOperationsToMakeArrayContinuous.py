import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        target = N - 1
        INF = 10 ** 20
        nums.sort()
        window = collections.deque()
        window_set = set()
        ans = INF
        for i in range(N):
            # nums[i] - X = target
            # X = nums[i] - target
            if nums[i] in window_set:
                continue
            ltarget = nums[i] - target
            window.append(nums[i])
            window_set.add(nums[i])
            while window[0] < ltarget:
                window_set.discard(window.popleft())
            ans = min(ans, N - len(window_set))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumNumberOfOperationsToMakeArrayContinuous(Solution):
    pass
