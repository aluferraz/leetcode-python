from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def isEqual(r1, r2):
            if r1 is None:
                return r2 is None
            if r2 is None:
                return r1 is None
            if r1.val == r2.val:
                return isEqual(r1.left, r2.left) and isEqual(r1.right, r2.right)
            return False

        def cloneTree(r):
            if r is None:
                return None
            clone = TreeNode(r.val)
            clone.left = cloneTree(r.left)
            clone.right = cloneTree(r.right)
            return clone

        def insert(node, value):
            if node is None:
                return TreeNode(value)
            if value < node.val:
                if node.left is None:
                    node.left = insert(node.left, value)
                else:
                    insert(node.left, value)
            else:
                if node.right is None:
                    node.right = insert(node.right, value)
                else:
                    insert(node.right, value)

        def delete(node, target):
            if node is None or target is None:
                return None

            if target.val < node.val:
                if node.left is not None and node.left.val == target.val:
                    node.left = None
                else:
                    delete(node.left, target)
            else:
                if node.right is not None and node.right.val == target.val:
                    node.right = None
                else:
                    delete(node.right, target)

        def find(node, value):
            if node is None:
                return None
            if value == node.val:
                return node
            if value < node.val:
                return find(node.left, value)
            else:
                return find(node.right, value)

        trees = []

        def build_trees(mask, root, nodes):
            if nodes == n:
                for t in trees:
                    if isEqual(root.right, t):
                        return
                trees.append(cloneTree(root.right))
                return
            for i in range(1, n + 1):
                if mask & (1 << i) == 0:
                    insert(root, i)
                    build_trees(mask | (1 << i), root, nodes + 1)
                    delete(root, find(root, i))

        build_trees(0, TreeNode(-1), 0)
        return trees


# leetcode submit region end(Prohibit modification and deletion)


class UniqueBinarySearchTreesIi(Solution):
    pass
