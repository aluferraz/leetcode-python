from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        number = 0
        while current is not None:
            number = (number * 10) + current.val
            current = current.next
        number *= 2
        new_head = ListNode(-1)
        current = new_head
        for d in str(number):
            current.next = ListNode(int(d))
            current = current.next
        return new_head.next


# leetcode submit region end(Prohibit modification and deletion)


class DoubleANumberRepresentedAsALinkedList(Solution):
    pass
