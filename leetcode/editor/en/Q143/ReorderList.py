from typing import List, Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None

        def get_second_half(head):
            slow = head
            fast = head.next
            while slow is not None and \
                    fast is not None and \
                    fast.next is not None and \
                    fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow
        def reverse_ll(head):
            if head is None:
                return None
            prev = None
            p1 = head
            p2 = head.next
            while p1 is not None:
                p1.next = prev
                prev = p1
                p1 = p2
                if p2 is not None:
                    p2 = p2.next
            return prev


        first_half_tail = get_second_half(head)
        second_half_head = first_half_tail.next
        first_half_tail.next = None
        second_half_head = reverse_ll(second_half_head)

        cur = head
        second_half_cur = second_half_head
        while cur is not None and second_half_cur is not None:
            bkp_first = cur.next
            bkp_second = second_half_cur.next
            to_be_inserted = second_half_cur
            to_be_inserted.next = None
            cur.next = to_be_inserted
            cur = cur.next
            cur.next = bkp_first
            cur = cur.next
            second_half_cur = bkp_second
        if second_half_cur is not None:
            cur = head
            while cur.next is not None:
                cur = cur.next
            cur.next = second_half_cur



# leetcode submit region end(Prohibit modification and deletion)


class ReorderList(Solution):
    pass
