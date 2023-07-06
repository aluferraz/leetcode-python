from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        def count(node, parent):
            if node is None:
                return (parent.val, 0)
            leftVal, resL = count(node.left, node)
            rightVal, resR = count(node.right, node)

            if leftVal == rightVal == node.val:
                return (node.val, 1 + resL + resR)
            return (20000, resL + resR)

        return count(root, None)[1]


# leetcode submit region end(Prohibit modification and deletion)


class CountUnivalueSubtrees(Solution):
    pass
