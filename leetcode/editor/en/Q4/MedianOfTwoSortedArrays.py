import math

import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        N = len(nums1)
        M = len(nums2)
        size = (N + M)
        arr = sorted(nums1 + nums2)
        if size % 2 == 0:
            return (arr[(size // 2) - 1] + arr[size // 2]) / 2
        return arr[size // 2]


# leetcode submit region end(Prohibit modification and deletion)


class MedianOfTwoSortedArrays(Solution):
    pass
