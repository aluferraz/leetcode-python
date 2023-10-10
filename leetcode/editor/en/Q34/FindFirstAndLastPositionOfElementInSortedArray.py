from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        N = len(nums)

        def bin_search_left(target):
            left = 0
            right = N - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    if nums[mid] == target:
                        ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        def bin_search_right(target):
            left = 0
            right = N - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        return [bin_search_left(target), bin_search_right(target)]


# leetcode submit region end(Prohibit modification and deletion)


class FindFirstAndLastPositionOfElementInSortedArray(Solution):
    pass
