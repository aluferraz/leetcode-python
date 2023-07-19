import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def alternatingSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        window = collections.deque()
        ans = -1
        window_elements = collections.defaultdict(int)
        for i in range(0, N):
            while len(window) > 0 and \
                    (not nums[i] == window[0] + (len(window) % 2)) or (
                    len(window_elements) == 2 and nums[i] not in window_elements):
                removed = window.popleft()
                window_elements[removed] -= 1
                if window_elements[removed] == 0:
                    window_elements.pop(removed)
                if len(window) == 0:
                    break
            window.append(nums[i])
            window_elements[nums[i]] += 1
            if len(window) >= 2:
                ans = max(ans, len(window))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LongestAlternatingSubarray(Solution):
    pass
