# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)
        cache = [[0 for _ in range(26)] for _ in range(N)]
        has_cache = [[False for _ in range(26)] for _ in range(N)]

        def go(prev, i):
            if i == N:
                return 0
            if has_cache[i][prev]:
                return cache[i][prev]
            cur = ord(s[i]) - ord('a')
            ans = 0
            if abs(cur - prev) <= k:
                ans = max(ans, 1 + go(cur, i + 1))
            ans = max(ans, go(prev, i + 1))
            has_cache[i][prev] = True
            cache[i][prev] = ans
            return ans

        ans = 0
        for i in range(N):
            ans = max(ans, go(ord(s[i]) - ord('a'), i))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LongestIdealSubsequence(Solution):
    pass
