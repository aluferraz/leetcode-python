import collections
import heapq
import math
from functools import cache
from math import gcd
from typing import List

import sortedcontainers
from sortedcontainers import SortedList


class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:

        to_use = [(-t, i) for i, t in enumerate(usageLimits)]
        to_use.sort()
        N = len(to_use)
        remaining_list = LinkedList()
        for i in range(len(to_use)):
            remaining_list.add_node(LLNode(to_use[i][1], -to_use[i][0]))
        ans = 0

        def go(prev):
            if remaining_list.get_size() < prev + 1:
                return 0
            left = remaining_list.head.value
            right = remaining_list.tail.value

            while left < right:
                mid = (left + right) // 2
                if mid in remaining_list.nodes or remaining_list.get_by_key(mid).value > 1:
                    right = mid
                else:
                    left = mid + 1
            start = left
            idx = start
            mask = 0
            for i in range(prev + 1):
                idx = (start + i) % remaining_list.get_size()
                remaining, number = to_use[idx]
                if mask & (1 << number) != 0:
                    return 0
                mask |= (1 << number)
                remaining += 1
                if remaining == 0:
                    to_use.pop(idx)
                    idx -= 1
                else:
                    to_use[idx] = (remaining, number)

            return 1 + go(prev + 1)

        return go(0)


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
