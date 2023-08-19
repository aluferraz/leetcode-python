from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        pos = 0
        for c in s:
            pos = t.find(c, pos)
            if pos == -1:
                return False
            pos += 1
        return True


# leetcode submit region end(Prohibit modification and deletion)


class IsSubsequence(Solution):
    pass
