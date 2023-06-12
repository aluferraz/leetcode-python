import collections
import heapq
from typing import List


# class Solution:
#     def minCost(self, nums: List[int], x: int) -> int:
#         costs = []
#         N = len(nums)
#         for i in range(N):
#             costs.append((nums[i], i))
#         costs.sort()
#
#         ans = 0
#         collected = set()
#
#         def choose(i):
#             if collected == N:
#                 return 0
#             minCost = costs[i]
#             if i > 0:
#
#         return choose(0)
class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:

        N = len(nums1)

        def condition(x):
            return x[1][0] + x[1][1], x[0]

        compress = []
        n1Sorted = []
        n2Sorted = []
        for i in range(N):
            compress.append((i, (nums1[i], nums2[i])))
            n1Sorted.append((nums1[i], i))
            n2Sorted.append((nums2[i], i))

        compress.sort(key=condition)
        n1Sorted.sort()
        n2Sorted.sort()

        def good(idx, q):
            i, (n1, n2) = compress[idx]
            if n1 >= q[0] and n2 >= q[1]:
                return True
            return False

        def findLeft(target, arr):
            left = 0
            right = N - 1
            ans = N
            while left <= right:
                mid = (left + right) // 2
                if arr[mid][0] >= target:
                    ans = arr[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        def find(q):
            minLeft = max(findLeft(q[0], n1Sorted), findLeft(q[1], n2Sorted))
            left = minLeft
            right = N
            ans = -1
            while left < right:
                mid = (left + right) // 2
                if good(mid, q, minLeft):
                    ans = mid
                    left = mid + 1
                else:
                    right = mid

            return ans

        ans = []
        for q in queries:
            possible = find(q)
            if possible >= N or possible == -1:
                ans.append(-1)
            else:
                ans.append(compress[possible][1][0] + compress[possible][1][1])

        return ans
