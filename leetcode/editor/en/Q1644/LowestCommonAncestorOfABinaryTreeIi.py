import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        level = 0
        pLevel = -1
        qLevel = -1
        parents = {}

        queue = collections.deque()

        queue.append((root, None))

        while len(queue) > 0 and (pLevel == -1 or qLevel == -1):
            size = len(queue)
            for _ in range(size):
                (node, parent) = queue.popleft()
                parents[node] = parent
                if node == q:
                    qLevel = level
                if node == p:
                    pLevel = level

                if node.left is not None:
                    if node.left == q:
                        parents[q] = node
                        qLevel = level + 1
                    if node.left == p:
                        parents[p] = node
                        pLevel = level + 1
                    queue.append((node.left, node))
                if node.right is not None:
                    if node.right == q:
                        parents[q] = node
                        qLevel = level + 1
                    if node.right == p:
                        parents[p] = node
                        pLevel = level + 1
                    queue.append((node.right, node))
            level += 1
        if pLevel == -1 or qLevel == -1:
            return None
        while pLevel != qLevel:
            if pLevel > qLevel:
                p = parents[p]
                pLevel -= 1
            if qLevel > pLevel:
                q = parents[q]
                qLevel -= 1

        while p != q:
            q = parents[q]
            p = parents[p]

        return p


# leetcode submit region end(Prohibit modification and deletion)


class LowestCommonAncestorOfABinaryTreeIi(Solution):
    pass
