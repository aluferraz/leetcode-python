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
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        ans = [ListNode(-1) for _ in range(k)]

        current = head
        ans_idx = 0
        size = 0
        while current is not None:
            size += 1
            current = current.next
        p_sizes = [(size // k) for _ in range(k)]
        size = size % k
        p_idx = 0
        while size > 0:
            p_sizes[p_idx] += 1
            size -= 1
            p_idx = (p_idx + 1) % k
        current = head
        ans_cnt = 0
        ans_current = ans[0]
        while current is not None:
            ans_current.next = ListNode(current.val)
            ans_current = ans_current.next
            ans_cnt += 1
            if ans_cnt == p_sizes[ans_idx]:
                ans_cnt = 0
                ans_idx = (ans_idx + 1) % k
                ans_current = ans[ans_idx]
            current = current.next
        for i in range(k):
            ans[i] = ans[i].next
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SplitLinkedListInParts(Solution):
    pass
