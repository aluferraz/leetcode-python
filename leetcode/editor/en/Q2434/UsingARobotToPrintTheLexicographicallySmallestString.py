# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def robotWithString(self, s: str) -> str:

        N = len(s)
        NLE = [N] * N
        stack = []
        for i in range(N):
            while len(stack) > 0 and s[i] <= s[stack[-1]]:
                NLE[stack.pop()] = i
            stack.append(i)
        t = []
        p = []
        i = 0
        remaining = collections.Counter(s)
        while i < N:
            for j in range(i, min(NLE[i] + 1, N)):
                t.append(s[j])
                remaining[s[j]] -= 1
                if remaining[s[j]] == 0:
                    remaining.pop(s[j])
                min_letter = "z"
                if remaining:
                    min_letter = min(remaining.keys())
                while len(t) and t[-1] <= min_letter:
                    p.append(t.pop())
            i = NLE[i] + 1
        return "".join(p)


# leetcode submit region end(Prohibit modification and deletion)


class UsingARobotToPrintTheLexicographicallySmallestString(Solution):
    pass
