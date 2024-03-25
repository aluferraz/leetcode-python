import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        vertical_map = collections.defaultdict(list)

        def bfs(node):
            if node is None:
                return
            q = collections.deque()
            q.append((node, 0))
            while len(q) > 0:
                size = len(q)
                for _ in range(size):
                    node, vlevel = q.popleft()
                    vertical_map[vlevel].append(node.val)
                    if node.left is not None:
                        q.append((node.left, vlevel - 1))
                    if node.right is not None:
                        q.append((node.right, vlevel + 1))

        bfs(root)
        vkeys = sorted(vertical_map.keys())
        ans = []
        for vlevel in vkeys:
            ans.append(vertical_map[vlevel])
        return ans
# leetcode submit region end(Prohibit modification and deletion)


class BinaryTreeVerticalOrderTraversal(Solution):
    pass