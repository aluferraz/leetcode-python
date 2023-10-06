import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        target = (N // 3) + 1
        cnt = collections.defaultdict(int)
        for n in nums:
            cnt[n] += 1
        return [k for k, v in cnt.items() if v >= target]


# leetcode submit region end(Prohibit modification and deletion)


class MajorityElementIi(Solution):
    pass
