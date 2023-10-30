from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        cache = [[0 for _ in range(5)] for _ in range(n + 1)]
        has_cache = [[False for _ in range(5)] for _ in range(n + 1)]
        idx_map = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        def go(c, k):
            if k == n:
                return 1
            if has_cache[k][idx_map[c]]:
                return cache[k][idx_map[c]]
            ans = 0
            if c == 'a':
                ans = 1 * go('e', k + 1)
            if c == 'e':
                ans = (1 * go('a', k + 1)) + (1 * go('i', k + 1))
            if c == 'i':
                ans = (1 * go('a', k + 1)) + \
                      (1 * go('e', k + 1)) + \
                      (1 * go('o', k + 1)) + \
                      (1 * go('u', k + 1))
            if c == 'o':
                ans = (1 * go('i', k + 1)) + (1 * go('u', k + 1))
            if c == 'u':
                ans = 1 * go('a', k + 1)
            has_cache[k][idx_map[c]] = True
            cache[k][idx_map[c]] = ans
            return ans

        ans = 0
        letters = ['a', 'e', 'i', 'o', 'u']
        for c in letters:
            ans += (1 * go(c, 1)) % MOD
        return ans % MOD
    # leetcode submit region end(Prohibit modification and deletion)


class CountVowelsPermutation(Solution):
    pass
