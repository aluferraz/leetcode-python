import collections
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        q = collections.deque()
        q.append(root)

        level = 0
        previous = -1
        while len(q) > 0:
            size = len(q)
            for _ in range(size):
                current = q.popleft()
                if level % 2 == 0 and (( previous >= 0 and current.val <= previous) or current.val % 2 == 0):
                    return False
                if level % 2 == 1 and (( previous >= 0 and current.val >= previous) or current.val % 2 == 1):
                    return False
                previous = current.val
                if current.left is not None:
                    q.append(current.left)
                if current.right is not None:
                    q.append(current.right)
            level += 1
            previous = -1

        return True


# leetcode submit region end(Prohibit modification and deletion)


class EvenOddTree(Solution):
    pass
