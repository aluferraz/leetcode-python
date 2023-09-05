import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minOperationsQueries(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        LOG_MAX = 20
        W_MAX = 27
        N = n
        adj_list = collections.defaultdict(set)

        for (u, v, w) in edges:
            adj_list[u].add((v, w))
            adj_list[v].add((u, w))
        edge_weights = {}

        def get_weights(node, parent, parent_w):
            if node == parent:
                return [0] * W_MAX
            current_weights = list(parent_w)
            edge_weights[node] = current_weights
            for (v, w) in adj_list[node]:
                if v == parent:
                    continue
                current_weights[w] += 1
                get_weights(v, node, current_weights)
                current_weights[w] -= 1

            return current_weights

        root = 0

        get_weights(root, -1, [0] * W_MAX)
        dp = [[0 for _ in range(LOG_MAX + 1)] for _ in range(N)]
        for i in range(N):
            dp[i][0] = i
        depth = [0 for _ in range(N)]

        def dfs(node, parent):
            dp[node][0] = parent
            for (v, w) in adj_list[node]:
                if v == parent:
                    continue
                depth[v] = depth[node] + 1
                dfs(v, node)

        dfs(root, root)

        for l in range(1, LOG_MAX):
            for i in range(N):
                dp[i][l] = dp[dp[i][l - 1]][l - 1]

        def get_lca(a, b):
            if depth[a] < depth[b]:
                return get_lca(b, a)
            must_go_up_levels = depth[a] - depth[b]
            for l in range(LOG_MAX, -1, -1):
                if must_go_up_levels & (1 << l):
                    a = dp[a][l]
            if a == b:
                return a
            for l in range(LOG_MAX, -1, -1):
                if dp[a][l] != dp[b][l]:
                    a = dp[a][l]
                    b = dp[b][l]
            return dp[a][0]

        ans = []
        for a, b in queries:
            lca = get_lca(a, b)
            len_between = depth[a] + depth[b] - (2 * depth[lca])
            combined_weigths = [edge_weights[a][i] + edge_weights[b][i] - (2 * edge_weights[lca][i]) for i in
                                range(W_MAX)]
            ans.append(len_between - max(combined_weigths))

        return ans

    # leetcode submit region end(Prohibit modification and deletion)


class MinimumEdgeWeightEquilibriumQueriesInATree(Solution):
    pass
