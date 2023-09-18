import collections
import heapq
import math
from functools import cache
from math import gcd
from typing import List, Optional

import sortedcontainers
from sortedcontainers import SortedList


# class Solution:
#     def countPairs(self, coordinates: List[List[int]], k: int) -> int:
#         N = len(coordinates)
#         ans = 0
#         for i in range(N):
#             for j in range(i + 1, N):
#                 if (coordinates[i][0] ^ coordinates[j][0]) + (coordinates[i][1] ^ coordinates[j][1]) == k:
#                     ans += 1
#         return ans

class Solution:
    def countWays(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        ans = 0
        for i in range(1, N - 1):
            if i > nums[i - 1]:
                ans += 1
        for i in range(N - 1, -1, -1):
            if i < nums[i]:
                ans += 1
        return ans


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


class Trie:

    def __init__(self, s=""):
        self.trie = {
            'wid': ''
        }
        self.ending_char = '*'
        if len(s) > 0:
            self.from_str(s)
        self.wids = set()

    def from_str(self, s):
        current = self.trie
        prev_wid = ""
        for char in s:
            if char not in current:
                # if prev_wid + char in self.wids:
                #     print("a")
                current[char] = {
                    'wid': prev_wid + char
                }
            current = current[char]
            prev_wid = current['wid']
            # self.wids.add(current['wid'])

        current[self.ending_char] = True
        current['wid'] = current['wid'] + self.ending_char
