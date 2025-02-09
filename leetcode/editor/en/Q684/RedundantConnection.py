import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parents = collections.defaultdict(-1)

        def find(i):
            path_comp = []
            while parents[i] >= 0:
                path_comp.append(i)
                i = parents[i]
            while path_comp:
                parents[path_comp.pop()] = i
            return i

        def union(i, j):
            if i == j:
                return
            if parents[j] < parents[i]:
                return union(j, i)
            parents[i] += parents[j]
            parents[j] = i

        ans = ()
        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv:
                ans = (u, v)
            else:
                union(pu, pv)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class RedundantConnection(Solution):
    pass
