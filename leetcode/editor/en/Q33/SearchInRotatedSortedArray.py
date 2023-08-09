from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        left = 0
        right = N - 1
        rotation_idx = N - 1
        while left <= right:
            mid = (left + right) // 2
            if mid + 1 < N and nums[mid] > nums[mid + 1]:
                rotation_idx = mid
                break
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1

        def bin_search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        return max(bin_search(0, rotation_idx), bin_search(rotation_idx + 1, N - 1))


# leetcode submit region end(Prohibit modification and deletion)


class SearchInRotatedSortedArray(Solution):
    pass
