import collections
import heapq
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        ans = []
        q = collections.deque([root])
        while q:
            size = len(q)
            level_sum = 0
            for _ in range(size):
                node = q.popleft()
                level_sum += node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            heapq.heappush(ans, -level_sum)

        if k >= len(ans):
            return -1

        for _ in range(k - 1):
            heapq.heappop(ans)
        return -heapq.heappop(ans)


# leetcode submit region end(Prohibit modification and deletion)


class KthLargestSumInABinaryTree(Solution):
    pass
