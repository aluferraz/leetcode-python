import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumLength(self, s: str) -> int:
        lmap = collections.defaultdict(collections.deque)
        N = len(s)
        for i in range(N):
            c = s[i]
            lmap[c].append(i)
        for i in range(26):
            c = chr(i + ord('a'))
            while len(lmap[c]) > 2:
                lmap[c].popleft()
                lmap[c].pop()
        remaining = []
        for c, idxs in lmap.items():
            while idxs:
                remaining.append((idxs.popleft(), c))
        return len(remaining)
        # remaining.sort()
        # ans = []
        # for _, c in remaining:
        #     ans.append(c)
        # return len(ans)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumLengthOfStringAfterOperations(Solution):
    pass
