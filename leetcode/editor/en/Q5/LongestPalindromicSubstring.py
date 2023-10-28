from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        ans = [0, 0]

        def compare(a, b):
            if (a[1] - a[0]) >= (b[1] - b[0]):
                return a
            return b

        def longest(i, j):
            ans = [i, i]
            while i >= 0 and j < N and s[i] == s[j]:
                ans = [i, j]
                i -= 1
                j += 1
            return ans

        for i in range(1, N):
            ans = compare(ans, longest(i - 1, i))
            ans = compare(ans, longest(i - 1, i + 1))
        return s[ans[0]:ans[1] + 1]


# leetcode submit region end(Prohibit modification and deletion)


class LongestPalindromicSubstring(Solution):
    pass
