import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = collections.Counter(nums)
        idx = 0
        for k in range(3):
            c = cnt[k]
            for i in range(c):
                nums[idx] = k
                idx += 1
        return idx


# leetcode submit region end(Prohibit modification and deletion)


class SortColors(Solution):
    pass
