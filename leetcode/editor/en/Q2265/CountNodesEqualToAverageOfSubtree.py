from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = 0

        def go(node):
            if node is None:
                return (0, 0)
            nonlocal ans
            leftCnt, leftSum = go(node.left)
            rightCnt, rightSum = go(node.right)
            totalSum = node.val + (leftSum + rightSum)
            totalCnt = 1 + (leftCnt + rightCnt)
            if (totalSum // totalCnt) == node.val:
                print(root.val)
                ans += 1
            return totalSum, totalCnt

        go(root)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class CountNodesEqualToAverageOfSubtree(Solution):
    pass
