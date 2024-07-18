from typing import List, Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = set()
        to_delete = set(to_delete)

        def go(node, nroot, p):
            if node is None:
                if nroot is not None:
                    ans.add(nroot)
                return
            if node.val in to_delete:
                if p is not None and node == p.left:
                    p.left = None
                    ans.add(nroot)
                elif p is not None and node == p.right:
                    p.right = None
                    ans.add(nroot)
                go(node.left, node.left, None)
                go(node.right, node.right, None)
            else:
                go(node.left, nroot, node)
                go(node.right, nroot, node)

        go(root, root, None)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class DeleteNodesAndReturnForest(Solution):
    pass
