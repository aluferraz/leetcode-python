# leetcode submit region begin(Prohibit modification and deletion)

class Node:
    def __init__(self, key, identifier):
        self.keys = set([key])
        self.id = identifier
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = Node("", float("-inf"))
        self.tail = Node("", float("inf"))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def inc(self, key: str) -> None:
        if key not in self.cache:
            if self.head.next.id == 1:
                self.cache[key] = self.head.next
                self.head.next.keys.add(key)
            else:
                new_entry = Node(key, 1)
                temp = self.head.next
                self.head.next = new_entry
                new_entry.prev = self.head
                new_entry.next = temp
                temp.prev = new_entry
                self.cache[key] = new_entry
        else:
            node = self.cache[key]
            node.keys.remove(key)
            if node.next.id == node.id + 1:
                self.cache[key] = node.next
                node.next.keys.add(key)
            else:
                new_entry = Node(key, node.id + 1)
                temp = node.next
                node.next = new_entry
                new_entry.prev = node
                new_entry.next = temp
                temp.prev = new_entry
                self.cache[key] = new_entry

            if len(node.keys) == 0:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.prev = None
                node.next = None

    def dec(self, key: str) -> None:
        node = self.cache[key]
        node.keys.remove(key)

        if node.id - 1 == 0:
            self.cache.pop(key)

        if node.prev.id == node.id - 1:
            self.cache[key] = node.prev
            node.prev.keys.add(key)
        elif node.id - 1 > 0:
            new_entry = Node(key, node.id - 1)
            temp = node.prev
            node.prev = new_entry
            new_entry.next = node
            temp.next = new_entry
            new_entry.prev = temp
            self.cache[key] = new_entry

        if len(node.keys) == 0:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None

    def getMaxKey(self) -> str:
        key = self.tail.prev.keys.pop()
        self.tail.prev.keys.add(key)
        return key

    def getMinKey(self) -> str:
        key = self.head.next.keys.pop()
        self.head.next.keys.add(key)
        return key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# leetcode submit region end(Prohibit modification and deletion)


class AllOoneDataStructure(AllOne):
    pass
