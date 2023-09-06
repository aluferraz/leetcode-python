from typing import List


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return head
        new_head = Node(-1)

        current = head
        current_new = new_head

        node_map = {}

        while current is not None:
            current_new.next = Node(current.val)
            current_new = current_new.next
            node_map[current] = current_new
            current = current.next

        current = head
        while current is not None:
            current_new = node_map[current]
            if current.random is not None:
                current_new.random = node_map[current.random]
            current = current.next
        return new_head.next


# leetcode submit region end(Prohibit modification and deletion)


class CopyListWithRandomPointer(Solution):
    pass
