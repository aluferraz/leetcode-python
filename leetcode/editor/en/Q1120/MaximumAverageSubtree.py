from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        ans = 0

        def go(node):
            if node is None:
                return (0, 0)
            nonlocal ans
            leftSum, leftCount = go(node.left)
            rightSum, rightCount = go(node.right)
            totalHere = [(node.val + leftSum + rightSum), (1 + leftCount + rightCount)]
            avgHere = totalHere[0] / totalHere[1]
            ans = max(ans, avgHere)
            return totalHere

        go(root)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


class MaximumAverageSubtree(Solution):
    pass
