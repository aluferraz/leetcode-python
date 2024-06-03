# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        N = len(s)
        M = len(t)

        cache = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                best = cache[i + 1][j]
                if s[i] == t[j]:
                    best = max(best, 1 + cache[i + 1][j + 1])
                best = max(best, cache[i + 1][j])
                cache[i][j] = best
        return M - cache[0][0]


# leetcode submit region end(Prohibit modification and deletion)


class AppendCharactersToStringToMakeSubsequence(Solution):
    pass
