from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def reverse(head):
            prev = None
            cur = head
            p2 = head.next

            while cur is not None:
                cur.next = prev
                prev = cur
                cur = p2
                if p2 is not None:
                    p2 = p2.next
            return prev

        l1 = reverse(l1)
        l2 = reverse(l2)

        carryOn = 0
        ans = ListNode(0)
        ans_pointer = ans
        while l1 is not None and l2 is not None:
            v1 = l1.val
            v2 = l2.val
            res = (v1 + v2 + carryOn)
            carryOn = res // 10
            ans_pointer.next = ListNode(res % 10)
            ans_pointer = ans_pointer.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            v1 = l1.val
            res = (v1 + carryOn)
            carryOn = res // 10
            ans_pointer.next = ListNode(res % 10)
            ans_pointer = ans_pointer.next
            l1 = l1.next

        while l2 is not None:
            v2 = l2.val
            res = (v2 + carryOn)
            carryOn = res // 10
            ans_pointer.next = ListNode(res % 10)
            ans_pointer = ans_pointer.next
            l2 = l2.next
        if carryOn != 0:
            ans_pointer.next = ListNode(carryOn)

        ans = ans.next
        ans = reverse(ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class AddTwoNumbersIi(Solution):
    pass
