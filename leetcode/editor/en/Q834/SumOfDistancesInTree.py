import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)
        N = n
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        count_nodes = [1] * N
        subtree_count = [0] * N
        ans = [0] * N

        def get_sum(node, parent):
            ans = 0
            for child in adj_list[node]:
                if child == parent:
                    continue
                get_sum(child, node)
                count_nodes[node] += count_nodes[child]
                subtree_count[node] += subtree_count[child] + count_nodes[child]
            return ans

        def fix_sum(node, parent):
            if parent != -1:
                base = subtree_count[parent]
                closer_nodes = count_nodes[node]
                further_nodes = N - closer_nodes
                subtree_count[node] = base - closer_nodes + further_nodes
            for child in adj_list[node]:
                if child == parent:
                    continue
                fix_sum(child, node)

        get_sum(0, -1)
        ans[0] = subtree_count[0]
        fix_sum(0, -1)
        return subtree_count


# leetcode submit region end(Prohibit modification and deletion)


class SumOfDistancesInTree(Solution):
    pass
