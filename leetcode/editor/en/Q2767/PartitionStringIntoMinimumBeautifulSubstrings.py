from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumBeautifulSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        @cache
        def can_partition(num):
            if num == 1:
                return True
            if num % 5 != 0 or num == 0:
                return False
            return can_partition(num // 5)

        N = len(s)
        INF = 10 ** 20

        @cache
        def go(left):
            if left == N:
                return 0
            if s[left] == '0':
                return INF
            ans = INF
            for right in range(left + 1, N + 1):
                bin_str = s[left:right]
                if can_partition(int(bin_str, 2)):
                    ans = min(ans, 1 + go(right))
            return ans

        best = go(0)
        if best >= INF:
            return -1
        return best


# leetcode submit region end(Prohibit modification and deletion)


class PartitionStringIntoMinimumBeautifulSubstrings(Solution):
    pass
