import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []

        def go(node):
            if node is None:
                return
            go(node.left)
            arr.append(node.val)
            go(node.right)

        go(root)
        cnt = collections.Counter(arr)
        modes = cnt.most_common()
        ans = []
        max_freq = -1
        for val, cnt in modes:
            if cnt < max_freq:
                break
            max_freq = cnt
            ans.append(val)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class FindModeInBinarySearchTree(Solution):
    pass
