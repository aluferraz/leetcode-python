from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.values = set()

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        self.values.add(root.val)
        if len(self.values) > 1:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

    # leetcode submit region end(Prohibit modification and deletion)


class UnivaluedBinaryTree(Solution):
    pass
