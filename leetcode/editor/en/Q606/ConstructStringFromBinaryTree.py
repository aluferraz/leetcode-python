from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """

        def go(node, ans):
            if node is None:
                return
            ans.append(str(node.val))
            if node.left is not None or node.right is not None:
                ans.append('(')
                go(node.left, ans)
                ans.append(')')
            if node.right is not None:
                ans.append('(')
                go(node.right, ans)
                ans.append(')')
            return ans

        return "".join(go(root, []))


# leetcode submit region end(Prohibit modification and deletion)


class ConstructStringFromBinaryTree(Solution):
    pass
