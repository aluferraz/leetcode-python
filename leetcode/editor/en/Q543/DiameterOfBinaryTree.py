from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def longest(node):
            if node is None:
                return 0
            nonlocal ans

            left_ans = longest(node.left)
            right_ans = longest(node.right)
            ans = max(ans, left_ans + right_ans)
            return 1 + max(left_ans, right_ans)

        longest(root)
        return ans





        
# leetcode submit region end(Prohibit modification and deletion)


class DiameterOfBinaryTree(Solution):
    pass