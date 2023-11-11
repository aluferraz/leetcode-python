import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        # N = len(adjacentPairs)
        seen = collections.defaultdict(int)
        adj_list = collections.defaultdict(set)
        nodes = set()
        for u, v in adjacentPairs:
            seen[v] += 1
            seen[u] += 1
            adj_list[u].add(v)
            adj_list[v].add(u)
            nodes.add(u)
            nodes.add(v)
        start_node = None
        for node in nodes:
            if seen[node] == 1:
                start_node = node
                break
        ans = []

        def dfs(node):
            if node is None:
                return
            ans.append(node)
            nodes.discard(node)
            for nnode in adj_list[node]:
                if nnode in nodes:
                    dfs(nnode)

        dfs(start_node)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class RestoreTheArrayFromAdjacentPairs(Solution):
    pass
