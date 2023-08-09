import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumSeconds(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dup = []
        INF = 10 ** 20
        for i in range(2):
            for n in nums:
                nums_dup.append(n)

        indices = collections.defaultdict(list)

        best_time = INF

        for i in range(len(nums_dup)):
            indices[nums_dup[i]].append(i)

        for idxes in indices.values():
            tot_time_here = 0
            prev = 0
            for i in idxes:
                tot_time_here = max((i - prev) // 2, tot_time_here)
                prev = i
            best_time = min(best_time, tot_time_here)
        return best_time


# leetcode submit region end(Prohibit modification and deletion)


class MinimumSecondsToEqualizeACircularArray(Solution):
    pass
