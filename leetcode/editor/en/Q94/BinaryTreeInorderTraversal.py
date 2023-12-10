from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def go(node, ans):
            if node is None:
                return
            go(node.left, ans)
            ans.append(node.val)
            go(node.right, ans)
            return ans

        return go(root, [])


# leetcode submit region end(Prohibit modification and deletion)


class BinaryTreeInorderTraversal(Solution):
    pass
