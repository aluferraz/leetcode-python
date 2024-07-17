from typing import List, Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        parents = {}
        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if isLeft == 1:
                if child in nodes:
                    nodes[parent].left = nodes[child]
                else:
                    nodes[parent].left = TreeNode(child)
                    nodes[child] = nodes[parent].left
            else:
                if child in nodes:
                    nodes[parent].right = nodes[child]
                else:
                    nodes[parent].right = TreeNode(child)
                    nodes[child] = nodes[parent].right
            parents[child] = parent
        root = None
        for node_key, node in nodes.items():
            if node_key not in parents:
                return node
        return root


# leetcode submit region end(Prohibit modification and deletion)


class CreateBinaryTreeFromDescriptions(Solution):
    pass
