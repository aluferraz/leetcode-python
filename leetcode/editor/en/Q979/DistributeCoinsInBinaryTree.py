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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        parents = {}
        levels = collections.defaultdict(collections.deque)
        enqueued = set()
        max_level = 0

        def get_parents(node, parent, level):
            if node is None:
                return
            nonlocal max_level
            max_level = max(max_level, level)
            levels[level].append(node)
            parents[node] = parent
            get_parents(node.left, node, level + 1)
            get_parents(node.right, node, level + 1)

            return

        get_parents(root, None, 0)
        ans = 0
        for level in range(max_level, -1, -1):
            queue = levels[level]
            while len(queue) > 0:
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()
                    parent = parents[node]
                    coins = node.val
                    if node.left is not None and node.left.val <= 0:
                        ans += abs(node.left.val)
                        coins += node.left.val
                    if node.right is not None and node.right.val <= 0:
                        ans += abs(node.right.val)
                        coins += node.right.val
                    if coins > 1:
                        node.val = 1
                        if parent is not None:
                            parent.val += (coins - 1)
                        ans += (coins - 1)
                    elif coins == 0:
                        node.val = -1
                    else:
                        node.val = coins
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class DistributeCoinsInBinaryTree(Solution):
    pass
