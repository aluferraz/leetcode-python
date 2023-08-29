import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class TreeAncestor(object):

    def __init__(self, n, parent):
        """
        :type n: int
        :type parent: List[int]
        """
        # https://www.youtube.com/watch?v=oib-XsjFa-M
        max_depth = 32  # 2 ^ 32

        dp = [[0 for _ in range(max_depth)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = parent[i]

        for l in range(1, max_depth):
            for i in range(n):
                dp[i][l] = dp[dp[i][l - 1]][l - 1]
        self.dp = dp
        adj_list = collections.defaultdict(list)

        for i in range(n):
            adj_list[parent[i]].append(i)

        depth = [0] * n

        def go(node, d):
            depth[node] = d
            for next_node in adj_list[node]:
                go(next_node, d + 1)

        go(0, 0)
        self.depth = depth

    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """

        if k > self.depth[node]:
            return -1
        bin_k = bin(k)[2::]
        bin_k_32 = [0] * 32
        i = 0
        bin_k = list(bin_k)
        while len(bin_k) > 0:
            bin_k_32[i] += int(bin_k.pop())
            i += 1
        current = node
        for i in range(32):
            if bin_k_32[i] == 1:
                current = self.dp[current][i]
        return current


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
# leetcode submit region end(Prohibit modification and deletion)


class KthAncestorOfATreeNode(TreeAncestor):
    pass
