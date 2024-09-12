import math
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        prev = head
        while current is not None:
            prev.next = ListNode(math.gcd(prev.val, current.val), current)
            prev = current
            current = current.next
        return head


# leetcode submit region end(Prohibit modification and deletion)


class InsertGreatestCommonDivisorsInLinkedList(Solution):
    pass
