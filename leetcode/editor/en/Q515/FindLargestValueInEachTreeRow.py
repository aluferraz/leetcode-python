import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        q = collections.deque()
        ans = []
        if root is None:
            return ans
        q.append(root.val)
        INF = 10 ** 20
        while len(q) > 0:
            size = len(q)
            level_max = -INF
            for _ in range(size):
                node = q.popleft()
                level_max = max(level_max, node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            ans.append(level_max)
        return ans

# leetcode submit region end(Prohibit modification and deletion)


class FindLargestValueInEachTreeRow(Solution):
    pass
