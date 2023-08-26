from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False
        N = len(s3)

        cache = {}

        def go(i, j, k):
            if i == N:
                return True
            if (j, k) in cache:
                return cache[(i, j, k)]
            ans = False
            if j < len(s1) and s1[j] == s3[i]:
                ans = ans or go(i + 1, j + 1, k)
            if k < len(s2) and s2[k] == s3[i]:
                ans = ans or go(i + 1, j, k + 1)
            cache[(j, k)] = ans
            return ans

        return go(0, 0, 0)
        # leetcode submit region end(Prohibit modification and deletion)


class InterleavingString(Solution):
    pass
