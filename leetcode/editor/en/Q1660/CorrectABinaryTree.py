import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def correctBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        q = collections.deque()
        q.append(root)
        parents = {}
        level = 0
        parents[root] = None
        wrong_node = None
        while len(q) > 0:
            size = len(q)
            next_level = set()
            for _ in range(size):
                node = q.popleft()
                if node in next_level:
                    wrong_node = parents[node]
                    next_level = set()
                    break

                if node.left is not None:
                    parents[node.left] = node
                    next_level.add(node.left)
                if node.right is not None:
                    parents[node.right] = node
                    next_level.add(node.right)
            for node in next_level:
                q.append(node)
            level += 1

        def build_tree(node):
            if node is None or node == wrong_node:
                return None
            new_root = TreeNode(node.val)
            new_root.right = build_tree(node.right)
            new_root.left = build_tree(node.left)
            return new_root

        return build_tree(root)


# leetcode submit region end(Prohibit modification and deletion)


class CorrectABinaryTree(Solution):
    pass
