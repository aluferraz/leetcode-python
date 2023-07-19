import collections
from typing import List

import sortedcollections


# leetcode submit region begin(Prohibit modification and deletion)
class LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = {}

    def add_node(self, node):
        node.next = None
        node.prev = None
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.nodes[node.key] = node

    def remove_node(self, node):
        if not node.key in self.nodes:
            return
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.nodes.pop(node.key)

    def get_by_key(self, key):
        if key in self.nodes:
            return self.nodes[key]
        return LLNode(-1, -1)

    def get_size(self):
        return len(self.nodes)


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.used_timeline = LinkedList()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.update_used(key)
        return self.used_timeline.get_by_key(key).value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.used_timeline.get_by_key(key)
        if node.value == -1:
            self.used_timeline.add_node(LLNode(key, value))
        else:
            node.value = value
            self.update_used(key)

        if self.used_timeline.get_size() > self.capacity:
            self.used_timeline.remove_node(self.used_timeline.head)

    def update_used(self, key):
        node = self.used_timeline.get_by_key(key)
        if node.value == -1:
            return
        self.used_timeline.remove_node(node)
        self.used_timeline.add_node(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)


class LruCache(LRUCache):
    pass
