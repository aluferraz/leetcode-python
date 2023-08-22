from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N = len(s)

        def go(i, pattern):
            if i == N:
                return True
            end = i + len(pattern)
            chunk = s[i:end]
            if chunk == pattern:
                return go(end, pattern)
            return False

        for i in range(1, (N // 2) + 1):
            if go(0, s[:i]):
                return True
        return False


# leetcode submit region end(Prohibit modification and deletion)


class RepeatedSubstringPattern(Solution):
    pass
