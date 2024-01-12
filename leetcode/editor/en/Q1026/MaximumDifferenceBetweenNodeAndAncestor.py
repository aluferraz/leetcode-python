from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def go(node, maxi, mini):
            if node is None:
                return 0
            diff = max(abs(node.val - maxi), abs(node.val - mini))
            diff = max(diff, go(node.left, max(node.val, maxi), min(node.val, mini)))
            diff = max(diff, go(node.right, max(node.val, maxi), min(node.val, mini)))
            return diff

        return go(root, root.val, root.val)



# leetcode submit region end(Prohibit modification and deletion)


class MaximumDifferenceBetweenNodeAndAncestor(Solution):
    pass