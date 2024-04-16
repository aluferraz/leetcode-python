from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def go(node, cur):
            if node is None:
                return 0
            nonlocal ans
            cur.append(str(node.val))
            if node.left is None and node.right is None:
                ans += int("".join(cur))
                cur.pop()
                return
            go(node.left,cur)
            go(node.right,cur)
            cur.pop()

        go(root, [])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SumRootToLeafNumbers(Solution):
    pass