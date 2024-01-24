import collections
from functools import cache
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:

        adj_list = collections.defaultdict(list)
        adj_list_rev = {}
        nodes = set()
        for u,v in edges:
            adj_list[u].append(v)
            adj_list_rev[v] = u
            nodes.add(u)
            nodes.add(v)
        ans = 1 if len(colors) > 0 else 0

        @cache
        def fill_valids(node, color):
            if colors[node] != color:
                return (False, -(10**20))
            count = 1
            for child in adj_list[node]:
                child_valid, child_count = fill_valids(child, color)
                if not child_valid:
                    return (False, -(10 ** 20))
                count += child_count
            return (True, count)

        for node in nodes:
            child_valid, child_count = fill_valids(node, colors[node])
            if child_valid:
                ans = max(ans, child_count)
        return ans













# leetcode submit region end(Prohibit modification and deletion)


class MaximumSubtreeOfTheSameColor(Solution):
    pass