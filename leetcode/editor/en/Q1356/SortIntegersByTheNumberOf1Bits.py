from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr.sort(key=lambda x: (x.bit_count(), x))
        return arr


# leetcode submit region end(Prohibit modification and deletion)


class SortIntegersByTheNumberOf1Bits(Solution):
    pass
