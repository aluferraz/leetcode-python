import math

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr)
        inc = int(math.ceil(N // 4))
        i = 0
        while i < N:
            ahead = min(i + inc, N - 1)
            if arr[i] == arr[ahead]:
                return arr[i]
            left = i
            right = ahead
            while left < right:
                mid = (left + right) // 2
                if arr[mid] > arr[i]:
                    right = mid
                else:
                    left = mid + 1
            i = left

        return arr[0]


# leetcode submit region end(Prohibit modification and deletion)


class ElementAppearingMoreThan25InSortedArray(Solution):
    pass
