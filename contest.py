import collections
import heapq
import math
from functools import cache
from math import gcd
from typing import List

import sortedcontainers
from sortedcontainers import SortedList


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        current = low
        ans = 0

        def get_number_sum(s):
            ns = 0
            for i in range(len(s) - 1):
                ns += int(s[i])
            return ns

        ans = set()

        def get_targets(sig):
            # sig - x = 1
            # x = sig - 1
            # sig - x = -1
            # x = sig + 1
            targets = set(
                [abs(sig + 1), abs(sig - 1)]
            )
            a = 0
            prepend = str(current)
            prepend = prepend[:len(prepend) - 1]
            for t in targets:
                if t >= 10:
                    continue
                if int(prepend + str(t)) >= int(current) and int(prepend + str(t)) <= int(high):
                    ans.add(int(prepend + str(t)))

        while int(current) <= int(high):
            if len(str(current)) == 1:
                for i in range(current, 11):
                    ans.add(i)
                current = 11
                continue
            sig = get_number_sum(str(current))
            # ans += get_targets(sig)
            get_targets(sig)
            current = int(current) + (10 - (int(current) % 10))

        return len(ans)


class SegTree:

    def __init__(self, arr):
        self.size = len(arr)
        self.segtree = [0 for _ in range(2 * self.size)]
        for i in range(self.size, len(self.segtree)):
            self.segtree[i] = arr[i - self.size]
        for i in range(self.size - 1, -1, -1):
            a = self.segtree[2 * i]
            b = self.segtree[(2 * i) + 1]
            self.segtree[i] = a + b

    def queryRange(self, left, right):
        left += self.size
        right += self.size
        ans = 0
        while left < right:

            if left % 2 == 1:
                ans += self.segtree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                ans += self.segtree[right]

            left //= 2
            right //= 2
        return ans

    def updateIndex(self, index, value):
        index += self.size
        self.segtree[index] = value
        while index > 1:
            index //= 2
            a = self.segtree[2 * index]
            b = self.segtree[2 * index + 1]
            self.segtree[index] = a + b


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
        self.nodes = collections.OrderedDict()

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
