import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        ins = collections.defaultdict(int)
        outs = collections.defaultdict(int)
        adj = {}
        for src, dst in pairs:
            if src in adj:
                adj[src].append(dst)
            else:
                adj[src] = collections.deque([dst])
            ins[dst] += 1
            outs[src] += 1

        start = None
        for i in outs:
            if outs[i] == ins[i] + 1:
                start = i
                break
        if start is None:
            start = pairs[0][0]

        ans = []
        stk = [start]
        while stk:
            if stk[-1] in adj and len(adj[stk[-1]]) > 0:
                stk.append(adj[stk[-1]].popleft())
            else:
                ans.append(stk.pop())

        ans = ans[::-1]
        res = []
        for i in range(1, len(ans)):
            res.append([ans[i - 1], ans[i]])
        return res


# leetcode submit region end(Prohibit modification and deletion)


class ValidArrangementOfPairs(Solution):
    pass
