from typing import List, Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def get_leafs(node, arr):
            if node is None:
                return arr
            if node.left is None and node.right is None:
                arr.append(node.val)
            get_leafs(node.left, arr)
            get_leafs(node.right, arr)
            return arr

        return get_leafs(root1,[]) == get_leafs(root2, [])

# leetcode submit region end(Prohibit modification and deletion)


class LeafSimilarTrees(Solution):
    pass