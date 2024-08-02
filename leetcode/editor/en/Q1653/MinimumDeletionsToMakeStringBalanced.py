# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        count_a = [0] * N
        count_b = [0] * N
        count_a[-1] = 1 if s[-1] == 'a' else 0
        count_b[0] = 1 if s[0] == 'b' else 0
        for i in range(1, N):
            count_b[i] = count_b[i - 1]
            if s[i] == 'b':
                count_b[i] += 1
        for i in range(N - 2, -1, -1):
            count_a[i] = count_a[i + 1]
            if s[i] == 'a':
                count_a[i] += 1
        ans = N
        for i in range(N - 1):
            tot_deletions = count_b[i] + count_a[i + 1]
            ans = min(tot_deletions, ans)
        ans = min(ans, count_b[-1], count_a[0])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumDeletionsToMakeStringBalanced(Solution):
    pass
