from typing import Optional

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node
        N = 0
        seen = set()
        cur = head
        min_node = head
        max_node = head
        while cur not in seen:
            N += 1
            seen.add(cur)
            if cur.val < min_node.val:
                min_node = cur
            if cur.val > max_node.val:
                max_node = cur
            cur = cur.next

        if insertVal <= min_node.val:
            cur = head
            while cur.next != min_node:
                cur = cur.next
            bkp = cur.next
            cur.next = Node(insertVal, bkp)
            return head
        if insertVal >= max_node.val:
            cur = head
            while cur != max_node:
                cur = cur.next
            while cur.next != cur and cur.next.val == max_node.val:
                cur = cur.next
            bkp = cur.next
            cur.next = Node(insertVal, bkp)
            return head
        inserted = False
        cur = head
        prev = None
        while not inserted:
            if prev is not None and insertVal >= prev.val and insertVal <= cur.val:
                prev.next = Node(insertVal, cur)
                return head
            prev = cur
            cur = cur.next
        return head


# leetcode submit region end(Prohibit modification and deletion)


class InsertIntoASortedCircularLinkedList(Solution):
    pass
