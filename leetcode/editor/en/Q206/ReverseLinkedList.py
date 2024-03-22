from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = None
        current = head
        while current is not None:
            p2 = current.next
            current.next = prev
            prev = current
            current = p2
        return prev


# leetcode submit region end(Prohibit modification and deletion)


class ReverseLinkedList(Solution):
    pass