from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow = head
        fast = head.next

        while fast is not None:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        return False

# leetcode submit region end(Prohibit modification and deletion)


class LinkedListCycle(Solution):
    pass
