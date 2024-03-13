from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        current = head
        previous = None
        while current is not None:
            total = 0
            ahead = current
            while ahead is not None:
                total += ahead.val
                if total == 0:
                    if previous is None:
                        return self.removeZeroSumSublists(ahead.next)
                    else:
                        previous.next = ahead.next
                        return self.removeZeroSumSublists(head)
                ahead = ahead.next
            previous = current
            current = current.next
        return head


        return head



# leetcode submit region end(Prohibit modification and deletion)


class RemoveZeroSumConsecutiveNodesFromLinkedList(Solution):
    pass