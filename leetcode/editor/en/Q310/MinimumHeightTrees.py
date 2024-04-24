import collections
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        leaf_nodes = []
        for k in adj_list.keys():
            if len(adj_list[k]) == 1:
                leaf_nodes.append(k)

        @cache
        def get_height(p, node):
            height = 0
            for child in adj_list[node]:
                if child != p:
                    height = max(height, 1 + get_height(node, child))
            return height

        ans = []
        min_height = n
        for i in range(n):
            height_here = get_height(i, i)
            if height_here < min_height:
                ans = []
            elif height_here > min_height:
                continue
            ans.append(i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumHeightTrees(Solution):
    pass
