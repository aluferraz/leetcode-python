from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if head is None:
            return [-1,-1]
        idxes = []
        idx = 0
        prev = head
        cur = head.next
        if cur is None or cur.next is None:
            return [-1,-1]
        next = cur.next

        while next is not None:
            if  cur.val < prev.val and cur.val < next.val:
                idxes.append(idx)
            elif cur.val > prev.val and cur.val > next.val:
                idxes.append(idx)
            prev = cur
            cur = next
            next = next.next
            idx += 1
        N = len(idxes)
        if N < 2:
            return [-1,-1]
        INF = 10 ** 20
        ans = [INF,-1]
        for i in range(1, N):
            ans[0] = min(ans[0], (idxes[i] - idxes[i-1]  + 1) )
            ans[1] = max(ans[1], (idxes[i] - idxes[0]  + 1))
        return ans



# leetcode submit region end(Prohibit modification and deletion)


class FindTheMinimumAndMaximumNumberOfNodesBetweenCriticalPoints(Solution):
    pass
    