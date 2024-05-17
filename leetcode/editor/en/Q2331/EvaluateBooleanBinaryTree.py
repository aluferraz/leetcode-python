from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def go(node):
            if node.right is None and node.left is None:
                return node.val == 1
            left_bool = go(node.left)
            right_bool = go(node.right)
            if node.val == 2:
                return left_bool or right_bool
            return left_bool and right_bool

        return go(root)


# leetcode submit region end(Prohibit modification and deletion)


class EvaluateBooleanBinaryTree(Solution):
    pass
