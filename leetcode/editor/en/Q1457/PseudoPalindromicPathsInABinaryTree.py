import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        ans = 0

        def go(node, path):
            if node is None:
                return
            path[node.val] += 1
            if node.left is None and node.right is None:
                odd = 0
                for v in path.values():
                    if v % 2 != 0:
                        odd += 1
                    if odd > 1:
                        break
                if odd <= 1:
                    nonlocal ans
                    ans += 1
            else:
                go(node.right, path)
                go(node.left, path)
            path[node.val] -= 1

        go(root, collections.Counter())

        return ans
        
# leetcode submit region end(Prohibit modification and deletion)


class PseudoPalindromicPathsInABinaryTree(Solution):
    pass