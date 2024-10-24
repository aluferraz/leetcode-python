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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        psum = collections.defaultdict(int)
        level_p = collections.defaultdict(set)

        def go(node, p, level):
            if node is None:
                return
            psum[p] += node.val
            level_p[level].add(p)
            go(node.left, node, level + 1)
            go(node.right, node, level + 1)

        go(root, None, 0)
        level_p_sum = collections.defaultdict(int)
        for k, v in level_p.items():
            for p in v:
                level_p_sum[k] += psum[p]

        q = collections.deque([(root, None)])
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                node, p = q.popleft()
                node.val = level_p_sum[level] - psum[p]
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
            level += 1
        return root


# leetcode submit region end(Prohibit modification and deletion)


class CousinsInBinaryTreeIi(Solution):
    pass
