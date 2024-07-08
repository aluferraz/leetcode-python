# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def go(node, arr):
            if node is None:
                return arr
            go(node.left, arr)
            arr.append(node.val)
            go(node.right, arr)
            return arr

        arr = go(root, [])
        new_root = TreeNode(-1)
        N = len(arr)

        def divide_and_conquer(node, left_bound, right_bound):
            if left_bound < 0 or right_bound >= N:
                return
            mid = (right_bound + left_bound) // 2
            if arr[mid] >= node.val:
                node.right = TreeNode(arr[mid])
                node = node.right
            else:
                node.left = TreeNode(arr[mid])
                node = node.left
            if mid - 1 >= left_bound:
                divide_and_conquer(node, left_bound, mid - 1)
            if mid + 1 <= right_bound:
                divide_and_conquer(node, mid + 1, right_bound)

        divide_and_conquer(new_root, 0, N - 1)
        return new_root.right


# leetcode submit region end(Prohibit modification and deletion)


class BalanceABinarySearchTree(Solution):

    def balanceBST(self, root: TreeNode) -> TreeNode:
        tree = TreeNode(1, None, TreeNode(15, TreeNode(14, TreeNode(7, TreeNode(2, None, TreeNode(3)),
                                                                    TreeNode(12, TreeNode(9, None, TreeNode(11))))),
                                          TreeNode(17)))
        return super().balanceBST(tree)
