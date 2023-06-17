import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """

        arr2.sort()
        N = len(arr1)
        M = len(arr2)

        def searchGreater(target):
            left = 0
            right = M
            while left < right:
                mid = (left + right) // 2
                if arr2[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        cache = {}

        def count(prev, i, arr):
            if i == N:
                return 0
            if (prev, i) in cache:
                return cache[(prev, i)]
            keep = 10 ** 20
            replace = 10 ** 20
            if arr[i] > prev:
                keep = count(arr[i], i + 1, arr)
            j = searchGreater(prev)
            if j < M:
                replace = 1 + count(arr2[j], i + 1, arr)
            cache[(prev, i)] = min(keep, replace)
            return cache[(prev, i)]

        ans = count(-1, 0, arr1)
        if ans > N:
            return -1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MakeArrayStrictlyIncreasing(Solution):
    pass
