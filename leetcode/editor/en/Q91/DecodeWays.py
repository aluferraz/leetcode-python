from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        s = [int(c) for c in s]

        cache = {}

        def go(must_combine, i):
            if i == N:
                return 1 if not must_combine else 0
            if (must_combine, i) in cache:
                return cache[(must_combine, i)]
            cur = s[i]
            ans = 0
            if must_combine:
                prev = (s[i - 1] * 10)
                combined = prev + cur
                if 1 <= combined <= 26:
                    ans = go(False, i + 1)
                else:
                    ans = 0
            else:
                if cur != 0:  # If cur is 0, we must combine it with the previous
                    ans = go(False, i + 1) \
                          + go(True, i + 1)
            cache[(must_combine, i)] = ans
            return ans

        return go(False, 0)


# leetcode submit region end(Prohibit modification and deletion)


class DecodeWays(Solution):
    pass
