from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        prev = None
        cur = head
        tail = head
        for _ in range(n):
            tail = tail.next
        if tail is None:
            return head.next
        while cur is not None:
            if tail is None:
                prev.next = cur.next
                cur.next = None
                break
            prev = cur
            cur = cur.next
            tail = tail.next
        return head

# leetcode submit region end(Prohibit modification and deletion)


class RemoveNthNodeFromEndOfList(Solution):
    pass