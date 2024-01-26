from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N = len(text1)
        M = len(text2)

        cache = [[0 for _ in range(M)] for _ in range(N)]
        has_cache = [[False for _ in range(M)] for _ in range(N)]
        def go(i,j):
            if i == N or j == M:
                return 0
            if has_cache[i][j]:
                return cache[i][j]
            ans = 0
            if text1[i] == text2[j]:
                ans = 1 + go(i+1, j+1)
            ans = max(ans, go(i, j+1))
            ans = max(ans, go(i+1, j))
            has_cache[i][j] = True
            cache[i][j] = ans
            return ans

        return go(0,0)

# leetcode submit region end(Prohibit modification and deletion)


class LongestCommonSubsequence(Solution):
    pass