from typing import List, Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur = list1
        acut = None
        bcut = None
        for _ in range(a-1):
            cur = cur.next
        acut = cur
        cur = list1
        for _ in range(b):
            cur = cur.next
        bcut = cur
        acut.next = list2
        tail = list2
        while tail.next is not None:
            tail = tail.next
        tail.next = bcut.next
        return list1


# leetcode submit region end(Prohibit modification and deletion)


class MergeInBetweenLinkedLists(Solution):
    pass
