from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr)
        left = 1
        right = N - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


# leetcode submit region end(Prohibit modification and deletion)


class PeakIndexInAMountainArray(Solution):
    pass
