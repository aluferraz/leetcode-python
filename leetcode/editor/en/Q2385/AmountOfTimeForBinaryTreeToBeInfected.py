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
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        target = None
        parents = collections.defaultdict(lambda x: None)
        infected = set()
        def find(node, parent):
            if node is None:
                return
            nonlocal target
            if node.val == start:
                target = node
            parents[node.val] = parent
            find(node.left, node)
            find(node.right, node)
        find(root, None)
        q = collections.deque()

        def enqueue(node):
            if node is not None and node.val not in infected:
                q.append(node)
                infected.add(node.val)

        t = 0
        enqueue(target)

        while len(q) > 0:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                infected.add(node.val)
                enqueue(node.left)
                enqueue(node.right)
                enqueue(parents[node.val])
            if len(q) > 0:
                t += 1
        return t


# leetcode submit region end(Prohibit modification and deletion)


class AmountOfTimeForBinaryTreeToBeInfected(Solution):
    pass