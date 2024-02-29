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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return root
        return self.bfs(root)
    def bfs(self, root):

        queue = collections.deque()
        queue.append(root)
        ans = None
        while len(queue) > 0:
            size = len(queue)
            ans = queue[0]
            for _ in range(size):
                current_node = queue.popleft()
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
        return ans.val

# leetcode submit region end(Prohibit modification and deletion)


class FindBottomLeftTreeValue(Solution):
    pass