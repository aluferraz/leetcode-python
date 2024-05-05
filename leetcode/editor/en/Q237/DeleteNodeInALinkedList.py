# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = None
        while node is not None:
            if node.next is None:
                prev.next = None
                break
            node.val = node.next.val
            prev = node
            node = node.next


# leetcode submit region end(Prohibit modification and deletion)


class DeleteNodeInALinkedList(Solution):
    pass
