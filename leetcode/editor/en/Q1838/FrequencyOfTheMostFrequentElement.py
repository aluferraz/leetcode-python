import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        used = 0
        N = len(nums)
        ans = 1
        q = collections.deque()
        q.append(nums[0])
        for i in range(1, N):
            d = nums[i] - q[-1]
            used += d * len(q)
            q.append(nums[i])
            while used > k:
                d = nums[i] - q.popleft()
                used -= d

            ans = max(ans, len(q))

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class FrequencyOfTheMostFrequentElement(Solution):
    pass
