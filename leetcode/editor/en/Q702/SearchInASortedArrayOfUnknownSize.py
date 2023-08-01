from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        out_of_bounds = (2 ** 31) - 1

        def find_size():
            left = 0
            right = 10 ** 5
            while left < right:
                mid = (left + right) // 2
                if reader.get(mid) == out_of_bounds:
                    right = mid
                else:
                    left = mid + 1
            return left

        left = 0
        right = find_size() - 1

        while left <= right:
            mid = (left + right) // 2
            number = reader.get(mid)
            if number == target:
                return mid
            if number > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)


class SearchInASortedArrayOfUnknownSize(Solution):
    pass
