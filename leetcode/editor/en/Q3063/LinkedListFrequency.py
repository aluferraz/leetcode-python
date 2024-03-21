import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = {}
        seen = []
        cur = head
        while cur is not None:
            if cur.val not in cnt:
                seen.append(cur.val)
                cnt[cur.val] = 0
            cnt[cur.val] += 1
            cur = cur.next
        ans = ListNode(0)
        cur = ans
        for v in seen:
            cur.next = ListNode(cnt[v])
            cur = cur.next
        return ans.next


# leetcode submit region end(Prohibit modification and deletion)


class LinkedListFrequency(Solution):
    pass