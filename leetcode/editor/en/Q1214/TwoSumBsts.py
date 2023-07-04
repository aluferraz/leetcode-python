from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """

        def find(target, node):
            if node is None:
                return False
            if node.val < target:
                return find(target, node.right)
            if node.val > target:
                return find(target, node.left)
            return True

        def checkSum(target, node):
            if node is None:
                return False
            return find(target - node.val, root2) or checkSum(target, node.left) or checkSum(target, node.right)

        return checkSum(target, root1)


# leetcode submit region end(Prohibit modification and deletion)


class TwoSumBsts(Solution):
    pass
