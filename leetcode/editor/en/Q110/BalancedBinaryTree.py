from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def height(node):
            if node is None:
                return 0
            leftHeight = height(node.left)
            rightHeight = height(node.right)
            if abs(leftHeight - rightHeight) > 1:
                return -10 ** 20
            return 1 + max(leftHeight, rightHeight)

        return height(root) >= 0


# leetcode submit region end(Prohibit modification and deletion)


class BalancedBinaryTree(Solution):
    pass
