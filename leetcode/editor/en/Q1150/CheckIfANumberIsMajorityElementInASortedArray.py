# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        counter = collections.Counter(nums)
        ans = counter.most_common(1)
        return ans[0][0] == target and ans[0][1] > (len(nums) // 2)

    # leetcode submit region end(Prohibit modification and deletion)


class CheckIfANumberIsMajorityElementInASortedArray(Solution):
    pass
