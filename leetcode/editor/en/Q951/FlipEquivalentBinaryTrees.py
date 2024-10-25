from functools import cache
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        @cache
        def go(node1, node2):
            if node1 is None or node2 is None:
                return node1 == node2
            if node1.val == node2.val:
                valid = go(node1.left, node2.left) and go(node1.right, node2.right)
                if not valid:
                    temp = node2.left
                    node2.left = node2.right
                    node2.right = temp
                    valid = go(node1.left, node2.left) and go(node1.right, node2.right)
                return valid
            return False

        return go(root1, root2)


# leetcode submit region end(Prohibit modification and deletion)


class FlipEquivalentBinaryTrees(Solution):
    pass
