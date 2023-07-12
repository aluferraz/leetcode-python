from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        class TreeNodeParent(TreeNode):
            def __init__(self, x, parent):
                super().__init__(x)
                self.parent = parent

        if root is None:
            return []

        def hydrate(node, parent):
            if node is None:
                return TreeNodeParent(None, parent)
            node_with_parent = TreeNodeParent(node.val, parent)
            node_with_parent.left = hydrate(node.left, node_with_parent)
            node_with_parent.right = hydrate(node.right, node_with_parent)
            return node_with_parent

        def find(node, target):
            if node is None:
                return None
            if node.val == target.val:
                return node
            ans = find(node.left, target)
            if ans is None:
                return find(node.right, target)
            return ans

        new_root = hydrate(root, None)
        start = find(new_root, target)
        if start is None:
            return []

        seen = set()

        def kDist(node, k, ans):
            if node in seen:
                return
            seen.add(node)
            if node is None or node.val is None:
                return
            if k == 0:
                ans.append(node.val)
                return

            kDist(node.left, k - 1, ans)
            kDist(node.right, k - 1, ans)
            kDist(node.parent, k - 1, ans)

        ans = []
        kDist(start, k, ans)
        return ans
    # leetcode submit region end(Prohibit modification and deletion)


class AllNodesDistanceKInBinaryTree(Solution):
    def distanceKHelper(self):
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        root.right = TreeNode(1)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)

        return super().distanceK(root, root.left, 2)
