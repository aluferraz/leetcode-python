from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        N = len(s)

        INF = 10 ** 20
        cache = [[INF for _ in range(N)] for _ in range(N)]
        has_cache = [[False for _ in range(N)] for _ in range(N)]

        def min_removal(l, r):
            if l >= r:
                return 0
            if has_cache[l][r]:
                return cache[l][r]
            head = s[l]
            tail = s[r]
            option_1, option_2, option_3 = INF, INF, INF
            if head == tail:
                option_1 = min_removal(l + 1, r - 1)
            option_2 = 1 + min_removal(l + 1, r)
            option_3 = 1 + min_removal(l, r - 1)
            ans = min(option_1, option_2, option_3)
            has_cache[l][r] = True
            cache[l][r] = ans
            return ans

        best = min_removal(0, N - 1)
        return best <= k


# leetcode submit region end(Prohibit modification and deletion)


class ValidPalindromeIii(Solution):
    pass
