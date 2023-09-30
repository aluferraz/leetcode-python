from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr = list(nums)
        arr.sort()
        if arr != nums:
            arr.reverse()
            if arr != nums:
                return False
        return True

        
# leetcode submit region end(Prohibit modification and deletion)


class MonotonicArray(Solution):
    pass
    