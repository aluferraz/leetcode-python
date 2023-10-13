from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        N = mountain_arr.length()

        def find_peak(left, right):
            while left <= right:
                mid = (left + right) // 2
                current = mountain_arr.get(mid)
                prev_el = mountain_arr.get(mid - 1)
                next_el = mountain_arr.get(mid - 1)
                if prev_el == current and next_el == current:
                    lans = find_peak(left, mid - 1)
                    rans = find_peak(mid + 1, right)
                    return max(lans, rans)

                if prev_el < current \
                        and next_el < current:
                    return mid
                elif prev_el < current and current < next_el:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        def bin_s_left(left, right, target):
            while left < right:
                mid = (left + right) // 2
                current = mountain_arr.get(mid)
                if current < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def bin_s_right(left, right, target):
            while left < right:
                mid = (left + right) // 2
                current = mountain_arr.get(mid)
                if current == target:
                    return mid
                elif current <= target:
                    right = mid
                else:
                    left = mid + 1

            return left

        peak_idx = find_peak(1, N - 2)
        lans = bin_s_left(0, peak_idx, target)
        if mountain_arr.get(lans) == target:
            return lans
        rans = bin_s_right(peak_idx, N, target)
        if rans == N:
            return -1
        if mountain_arr.get(rans) == target:
            return rans
        return -1


# leetcode submit region end(Prohibit modification and deletion)


class FindInMountainArray(Solution):
    pass
