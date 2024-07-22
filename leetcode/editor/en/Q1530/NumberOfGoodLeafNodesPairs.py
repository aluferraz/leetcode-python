# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        parents = {}
        leaf_nodes = {}

        def get_parents(node, p):
            if node is None:
                return
            parents[node] = p
            get_parents(node.left, node)
            get_parents(node.right, node)
            if node.left is None and node.right is None:
                leaf_nodes[node] = node

        get_parents(root, None)

        for _ in range(distance // 2):
            for node in leaf_nodes:
                if leaf_nodes[node] != root:
                    leaf_nodes[node] = parents[leaf_nodes[node]]

        current_pos = collections.defaultdict(int)
        for node, pos in leaf_nodes.items():
            current_pos[pos] += 1

        ans = 0
        for pos, cnt in current_pos.items():
            if cnt > 1:
                ans += cnt
            if distance % 2 == 1 and parents[pos] in current_pos and current_pos[parents[pos]] > 0:
                ans += (cnt + current_pos[parents[pos]])

        return (ans // 2)


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfGoodLeafNodesPairs(Solution):
    def countPairs(self, root: TreeNode, distance: int) -> int:
        tree = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
        return super().countPairs(tree, 3)
