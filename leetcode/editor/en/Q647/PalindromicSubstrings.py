from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        ans = 0

        cache = [[False for _ in range(N)] for _ in range(N)]
        has_cache = [[False for _ in range(N)] for _ in range(N)]
        def is_palindrome(l, r):
            if l >= r:
                return True
            if s[l] != s[r]:
                return False
            if has_cache[l][r]:
                return cache[l][r]
            has_cache[l][r] = True
            cache[l][r] = is_palindrome(l+1, r-1)
            return cache[l][r]

        for i in range(N):
            for j in range(i,N):
                if is_palindrome(i,j):
                    ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class PalindromicSubstrings(Solution):
    pass