import collections
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        monoqueue = collections.deque()
        current = head
        while current is not None:
            while len(monoqueue) > 0 and current.val > monoqueue[-1].val:
                monoqueue.pop()
            monoqueue.append(current)
            current = current.next
        monoqueue.append(None)
        new_head = monoqueue.popleft()
        current = new_head
        while current is not None:
            current.next = monoqueue.popleft()
            current = current.next
        return new_head


# leetcode submit region end(Prohibit modification and deletion)


class RemoveNodesFromLinkedList(Solution):
    pass
