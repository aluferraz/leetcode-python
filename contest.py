import collections
import heapq
import math
from functools import cache
from math import gcd
from typing import List

import sortedcontainers


class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        N = len(nums)
        maxEl = max(nums)
        distribution = [1 for _ in range(maxEl + 1)]
        distribution[0] = 0
        ans = 0
        for i in range(N):
            segTree = SegTree(distribution)
            segTree.updateIndex(nums[i], 0)
            left = nums[i]
            right = nums[i]
            for j in range(i + 1, N):
                segTree.updateIndex(nums[j], 0)
                left = min(nums[j], left)
                right = max(nums[j], right)
                ans = ans + segTree.queryRange(left, right)
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
