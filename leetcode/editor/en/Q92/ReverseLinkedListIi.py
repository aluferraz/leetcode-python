from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        pos = 1
        prev = None
        current = head
        while pos < left:
            prev = current
            current = current.next
            pos += 1
        slice_head = current
        slice_previous = prev
        if slice_previous is not None:
            slice_previous.next = None

        while pos < right:
            prev = current
            current = current.next
            pos += 1
        slice_tail = current
        after_slice = slice_tail.next
        if slice_tail is not None:
            slice_tail.next = None

        def rev_ll(lhead):
            prev = None
            current = lhead
            next_node = lhead.next

            while current is not None:
                current.next = prev
                prev = current
                current = next_node
                if next_node is not None:
                    next_node = next_node.next
            return prev
        if slice_previous is not None:
            slice_previous.next = rev_ll(slice_head)
        else:
            head = rev_ll(slice_head)
        current = head
        while current is not None and current.next is not None:
            current = current.next
        if current is not None:
            current.next = after_slice
        return head


# leetcode submit region end(Prohibit modification and deletion)


class ReverseLinkedListIi(Solution):
    pass
