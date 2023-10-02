import collections
import heapq
import math
from functools import cache
from math import gcd
from typing import List, Optional

import sortedcontainers
from sortedcontainers import SortedList

upper = 10 ** 6


def prime_sieve(n):
    primes = [True for _ in range(n + 1)]
    primes[0] = False
    primes[1] = False

    limit = int(math.sqrt(n))
    for i in range(2, limit + 1):
        if primes[i]:
            j = 2
            while j * i <= n:
                primes[j * i] = False
                j += 1
    ans = [
        i for i in range(len(primes)) if primes[i]
    ]
    return ans


#
# primes = set(prime_sieve(upper))
class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        N = len(edges)
        adj_list = collections.defaultdict(list)

        def kahn():
            in_degree = [0] * N

            for i in range(N):
                from_node = i
                to_node = edges[i]
                adj_list[from_node].append(to_node)
                in_degree[to_node] += 1

            q = collections.deque()
            for i in range(N):
                if in_degree[i] == 0:
                    q.append(i)

            while len(q) > 0:
                size = len(q)
                for _ in range(size):
                    node = q.popleft()
                    for next_node in adj_list[node]:
                        in_degree[next_node] -= 1
                        if in_degree[next_node] == 0:
                            q.append(next_node)
            return in_degree

        in_degree = kahn()
        has_cycle = [x != 0 for x in in_degree]
        cycle_size = [0] * N

        def get_cycle_size(i, seen, size):
            if i in seen:
                return size
            seen.add(i)
            cycle_size_here = 0
            for j in adj_list[i]:
                cycle_size_here = get_cycle_size(j, seen, size + 1)
            cycle_size[i] = cycle_size_here
            return cycle_size_here

        for i in range(N):
            if has_cycle[i] and cycle_size[i] == 0:
                get_cycle_size(i, set(), 0)

        @cache
        def dfs(i):
            if has_cycle[i]:
                return cycle_size[i]
            ans = 1
            for next_node in adj_list[i]:
                ans += dfs(next_node)
            return ans

        ans = []
        for i in range(N):
            ans.append(dfs(i))
        return ans

        # has_cache = [False] * N


#
# has_cache[-1] = True
# cache[-1] = nums[-1]
#
# def go(i, r, a):
#     if i < 0:
#         return 0
#     score_here = nums[i]
#     score_ahead = nums[i]
#     if i + 1 < r:
#         score_ahead = a
#     include_here = (score_here & score_ahead)
#     ans = 0
#     if include_here <= score_ahead and include_here <= score_here:
#         ans = 1 + go(i - 2, i, nums[i - 1])
#     ans = max(ans, go(i - 1, r, a))
#
#     return ans
#
# return go(N - 1, N - 1, nums[-1])

# prefix_and = [0] * N
# prefix_sum = [0] * N
# prefix_and[0] = nums[0]
# prefix_sum[0] = nums[0]
# for i in range(1, N):
#     prefix_and[i] = prefix_and[i - 1] & nums[i]
#     prefix_sum[i] = prefix_sum[i - 1] + prefix_and[i]
# ans = prefix_sum[-1]
#
# def go(l,r):
#     if i == N:
#         return 0
#
#     split_here =


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
