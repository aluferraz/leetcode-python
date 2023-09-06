from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        head = TreeNode(-1, None, None)
        current = head

        def preorder(node):
            if node is None:
                return None
            nonlocal current
            current.right = TreeNode(node.val, None, None)
            current = current.right

            preorder(node.left)
            preorder(node.right)

        preorder(root)

        current = head.right
        current_ori = root
        while current is not None:
            current_ori.val = current.val
            current_ori.left = None
            current = current.right
            if current is not None:
                current_ori.right = TreeNode(-1)
                current_ori = current_ori.right


# leetcode submit region end(Prohibit modification and deletion)


class FlattenBinaryTreeToLinkedList(Solution):
    pass
