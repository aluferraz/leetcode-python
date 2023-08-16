from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        if head is None:
            return None
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = ListNode(-1)
        h2 = ListNode(-1)

        current = head
        nextBackup = head.next
        h1Current = h1
        h2Current = h2

        while current is not None:
            nextBackup = current.next
            current.next = None
            if current.val < x:
                h1Current.next = current
                h1Current = h1Current.next
            else:
                h2Current.next = current
                h2Current = h2Current.next
            current = nextBackup

        h1Current.next = h2.next
        return h1.next


# leetcode submit region end(Prohibit modification and deletion)


class PartitionList(Solution):
    pass
