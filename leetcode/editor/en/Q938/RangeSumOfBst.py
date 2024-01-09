from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        arr = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)
        N = len(arr)
        ans = 0
        l = 0
        r = N
        start = -1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] == low:
                start = mid
                break
            elif arr[mid] < low:
                l = mid + 1
            else:
                r = mid - 1

        for i in range(start,N):
            ans += arr[i]
            if arr[i] == high:
                break
        return ans
# leetcode submit region end(Prohibit modification and deletion)


class RangeSumOfBst(Solution):
    pass