from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """
        d = max(abs(sx - fx), abs(sy - fy))
        if d == 0 and t == 1:
            return False
        return d <= t


# leetcode submit region end(Prohibit modification and deletion)


class DetermineIfACellIsReachableAtAGivenTime(Solution):
    pass
